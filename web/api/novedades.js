// Últimas circulares, resoluciones y oficios publicados en www.sii.cl (en vivo, caché 6 h en el CDN).
const UA = { "User-Agent": "Mozilla/5.0 (compatible; FiscolItA/1.0)" };

const ENT = { aacute: "á", eacute: "é", iacute: "í", oacute: "ó", uacute: "ú", Aacute: "Á", Eacute: "É", Iacute: "Í", Oacute: "Ó",
  Uacute: "Ú", ntilde: "ñ", Ntilde: "Ñ", deg: "°", ordm: "º", ordf: "ª", uuml: "ü", nbsp: " ", amp: "&", quot: '"', laquo: "«", raquo: "»", ndash: "–", mdash: "—", ldquo: "“", rdquo: "”", lsquo: "‘", rsquo: "’", hellip: "…", iexcl: "¡", iquest: "¿" };
const limpiar = (s) => s.replace(/<[^>]+>/g, "").replace(/&(\w+);/g, (m, e) => ENT[e] ?? m)
  .replace(/&#(\d+);/g, (_, n) => String.fromCharCode(+n)).replace(/\s+/g, " ").trim();

async function indice(tipo, anio, n) {
  const url = tipo === "circulares"
    ? `https://www.sii.cl/normativa_legislacion/circulares/${anio}/indcir${anio}.htm`
    : `https://www.sii.cl/normativa_legislacion/resoluciones/${anio}/res_ind${anio}.htm`;
  const r = await fetch(url, { headers: UA });
  if (!r.ok) return [];
  const html = new TextDecoder("latin1").decode(await r.arrayBuffer());
  const out = [];
  const re = /<h5[^>]*>\s*<a href=['"]([^'"]+\.pdf)['"][^>]*>([\s\S]*?)<\/a>\s*<\/h5>\s*<p[^>]*>([\s\S]*?)<\/p>/gi;
  let m;
  while ((m = re.exec(html)) && out.length < n) {
    out.push({ tipo: tipo === "circulares" ? "Circular" : "Resolución", titulo: limpiar(m[2]), detalle: limpiar(m[3]), url: new URL(m[1].trim(), url).href });
  }
  return out;
}

async function oficios(anio, n) {
  const todos = [];
  for (const key of ["RENTA", "IVA", "OTROS"]) {
    try {
      const r = await fetch("https://www3.sii.cl/getPublicacionesCTByMateria", {
        method: "POST", headers: { ...UA, "Content-Type": "application/json" }, body: JSON.stringify({ key, year: String(anio) }) });
      if (r.ok) for (const it of await r.json()) todos.push({ ...it, _k: key });
    } catch {}
  }
  const f = (s) => { const [d, m, a] = s.split("/"); return new Date(+a, +m - 1, +d).getTime(); };
  todos.sort((a, b) => f(b.pubFechaPubli) - f(a.pubFechaPubli));
  return todos.slice(0, n).map((it) => ({
    tipo: `Oficio ${it._k}`, titulo: `${it.tipoArchPublica || "Oficio"} N° ${it.pubNumOficio} de ${it.pubFechaPubli}`,
    detalle: limpiar(it.pubResumen || ""), url: "https://www.sii.cl/normativa_legislacion/jurisprudencia_administrativa/indice_jadm.htm" }));
}

export default async function handler(req, res) {
  const anio = new Date().getFullYear();
  const n = Math.min(parseInt(req.query?.n || "4", 10) || 4, 10);
  try {
    const [c, r, o] = await Promise.all([indice("circulares", anio, n), indice("resoluciones", anio, n), oficios(anio, n)]);
    res.setHeader("Cache-Control", "s-maxage=21600, stale-while-revalidate=86400");
    res.status(200).json({ actualizado: new Date().toISOString(), circulares: c, resoluciones: r, oficios: o });
  } catch (e) {
    res.status(502).json({ error: "No se pudo consultar www.sii.cl en este momento." });
  }
}
