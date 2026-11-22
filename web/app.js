// FiscolItA · simuladores, indicadores, calendario y novedades (todo en el navegador salvo /api/novedades).
const NADA = new Proxy({}, { get: () => undefined, set: () => true });
const $ = (s) => document.querySelector(s) || NADA;   // en páginas sin ese bloque, no hace nada
const clp = (n) => "$" + Math.round(n).toLocaleString("es-CL");
const num = (s) => {
  s = String(s ?? "").replace(/[$\s]/g, "");
  if (s.includes(",")) s = s.replace(/\./g, "").replace(",", ".");
  else if (/^\d{1,3}(\.\d{3})+$/.test(s)) s = s.replace(/\./g, "");
  const n = parseFloat(s);
  return isNaN(n) ? 0 : n;
};
const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));

// ---------- valores de respaldo (si no hay conexión a mindicador.cl) ----------
const IND = { uf: 41377.93, utm: 72440, usd: 1008.79, eur: 1107.59, fecha: "2026-11-21", vivo: false };
const BHE = { 2025: 14.5, 2026: 15.25, 2027: 16, 2028: 17 };            // sii.cl/destacados/boletas_honorarios
const INTERES = { tasa: 7.70, fuente: "Res. Ex. SII N° 88 de 2026 (2° semestre 2026)", url: "https://www.sii.cl/normativa_legislacion/resoluciones/2026/reso88.pdf" };
const TRAMOS = [[13.5, 0], [30, .04], [50, .08], [70, .135], [90, .23], [120, .304], [310, .35], [Infinity, .40]]; // art. 43 N° 1 LIR

const hoy = new Date();
const fHoy = hoy.toLocaleDateString("es-CL", { weekday: "long", day: "numeric", month: "long" });
$("#hoy").textContent = fHoy.charAt(0).toUpperCase() + fHoy.slice(1);

async function indicadores() {
  try {
    const r = await fetch("https://mindicador.cl/api", { cache: "no-store" });
    const d = await r.json();
    Object.assign(IND, { uf: d.uf.valor, utm: d.utm.valor, usd: d.dolar.valor, eur: d.euro.valor, vivo: true,
      f: { uf: d.uf.fecha, utm: d.utm.fecha, usd: d.dolar.fecha, eur: d.euro.fecha } });
  } catch {}
  const f = (k) => IND.f ? new Date(IND.f[k]).toLocaleDateString("es-CL", k === "utm" ? { month: "long", year: "numeric", timeZone: "UTC" } : { day: "2-digit", month: "2-digit", timeZone: "UTC" }) : "referencial";
  const dec = (n) => "$" + n.toLocaleString("es-CL", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  $("#v-uf").textContent = dec(IND.uf); $("#f-uf").textContent = f("uf");
  $("#v-utm").textContent = clp(IND.utm); $("#f-utm").textContent = f("utm");
  $("#v-usd").textContent = dec(IND.usd); $("#f-usd").textContent = f("usd") + " · Banco Central";
  $("#v-eur").textContent = dec(IND.eur); $("#f-eur").textContent = f("eur") + " · Banco Central";
  render();
}

// ---------- simuladores ----------
const SIMS = {
  bhe: {
    t: "Boleta de honorarios", d: "Retención que el pagador hace al boletear.",
    campos: [["monto", "Monto", "1.000.000"], ["modo", "El monto es", null, [["bruto", "Bruto (total honorarios)"], ["liquido", "Líquido que quiero recibir"]]]],
    calc: (v) => {
      const anio = hoy.getFullYear(), tasa = BHE[anio] ?? (anio > 2028 ? 17 : 14.5), t = tasa / 100;
      const bruto = v.modo === "liquido" ? num(v.monto) / (1 - t) : num(v.monto), ret = Math.round(bruto * t);
      return { filas: [["Bruto (total honorarios)", clp(bruto)], [`Retención ${String(tasa).replace(".", ",")}%`, clp(ret)]], total: ["Líquido a recibir", clp(bruto - ret)],
        fuente: [`Retención vigente en ${anio}`, "https://www.sii.cl/destacados/boletas_honorarios/"] };
    },
  },
  ppm: {
    t: "PPM", d: "Pago provisional mensual que va en el F29.",
    campos: [["base", "Ingresos brutos del mes sin IVA", "10.000.000"], ["tasa", "Tasa PPM (%)", "0,25"]],
    calc: (v) => ({ filas: [["Base imponible (cód. 563)", clp(num(v.base))], ["Tasa (cód. 115)", String(v.tasa || 0) + "%"]],
      total: ["PPM a pagar (cód. 62)", clp(num(v.base) * num(v.tasa) / 100)], fuente: ["Art. 84 Ley sobre Impuesto a la Renta · F29 línea 69", "https://www.sii.cl/preguntas_frecuentes/impuestos_mensuales/001_130_1908.htm"] }),
  },
  iva: {
    t: "IVA del mes", d: "Débito de tus ventas menos crédito de tus compras (19%).",
    campos: [["ventas", "Ventas netas del mes", "5.000.000"], ["compras", "Compras netas con factura", "2.000.000"]],
    calc: (v) => {
      const deb = num(v.ventas) * .19, cred = num(v.compras) * .19, n = deb - cred;
      return { filas: [["Débito fiscal", clp(deb)], ["Crédito fiscal", clp(cred)]], total: n >= 0 ? ["IVA a pagar", clp(n)] : ["Remanente para el mes siguiente", clp(-n)],
        fuente: ["Arts. 14, 20 y 23 DL 825", "https://www.bcn.cl/leychile/navegar?idNorma=6369"] };
    },
  },
  multa: {
    t: "Multa por atraso", d: "Declarar fuera de plazo un impuesto que se debía pagar.",
    campos: [["imp", "Impuesto adeudado", "500.000"], ["meses", "Meses de atraso", "3"]],
    calc: (v) => {
      const imp = num(v.imp), m = Math.max(1, Math.round(num(v.meses))), pct = m <= 5 ? 10 : Math.min(10 + 2 * (m - 5), 30);
      const interes = imp * INTERES.tasa / 100 / 360 * m * 30;
      return { filas: [[`Multa art. 97 N° 2 (${pct}%)`, clp(imp * pct / 100)], [`Interés penal aprox. (${String(INTERES.tasa).replace(".", ",")}% anual)`, clp(interes)]],
        total: ["Total aprox. con el impuesto", clp(imp * (1 + pct / 100) + interes)],
        nota: "No incluye reajuste IPC. Si el impuesto es de retención o recargo (como el IVA) y no se pagó, aplica el art. 97 N° 11. El SII suele condonar parte si regularizas antes de una fiscalización.",
        fuente: [`Art. 97 N° 2 y art. 53 del Código Tributario · ${INTERES.fuente}`, INTERES.url] };
    },
  },
  sueldo: {
    t: "Impuesto de un sueldo", d: "Impuesto único de segunda categoría del mes.",
    campos: [["renta", "Renta líquida imponible", "2.500.000"]],
    calc: (v) => {
      const r = num(v.renta), u = IND.utm; let imp = 0, ant = 0; const filas = [];
      for (const [lim, t] of TRAMOS) { const tope = lim * u;
        if (r > ant && t) { const p = Math.min(r, tope) - ant; imp += p * t; filas.push([`${clp(ant)} a ${clp(Math.min(r, tope))} × ${String(t * 100).replace(".", ",")}%`, clp(p * t)]); }
        ant = tope; if (r <= tope) break; }
      if (!filas.length) filas.push(["Exento (hasta 13,5 UTM)", clp(0)]);
      return { filas, total: [`Impuesto del mes (${r ? (imp / r * 100).toFixed(2).replace(".", ",") : 0}% efectivo)`, clp(imp)],
        nota: "Renta líquida imponible = sueldo imponible menos AFP, salud y seguro de cesantía. UTM del mes: " + clp(u) + ".",
        fuente: ["Art. 43 N° 1 Ley sobre Impuesto a la Renta", "https://www.sii.cl/valores_y_fechas/impuesto_2da_categoria/impuesto2026.htm"] };
    },
  },
  conv: {
    t: "Calculadora UF / USD / EUR / UTM", d: "Convierte a pesos con los valores del día.",
    campos: [["monto", "Cantidad", "15"]],
    calc: (v) => { const n = num(v.monto);
      return { filas: [[`${v.monto || 0} UF`, clp(n * IND.uf)], [`${v.monto || 0} USD`, clp(n * IND.usd)], [`${v.monto || 0} EUR`, clp(n * IND.eur)], [`${v.monto || 0} UTM`, clp(n * IND.utm)]],
        fuente: [IND.vivo ? "UF y UTM: SII · USD y EUR: Banco Central (vía mindicador.cl)" : "Valores referenciales sin conexión", "https://www.sii.cl/valores_y_fechas/"] }; },
  },
};
let actual = document.body.dataset.sim || "bhe";
const valores = {};

function tabs() {
  $("#tabs").innerHTML = Object.entries(SIMS).map(([k, s]) =>
    `<button class="tab" role="tab" aria-selected="${k === actual}" data-k="${k}">${s.t}</button>`).join("");
  $("#tabs").onclick = (e) => { const k = e.target.dataset?.k; if (k) { actual = k; tabs(); panel(); } };
}

const PAGINA = { bhe: "calculadora-boleta-honorarios", ppm: "calculadora-ppm", iva: "calculadora-iva", multa: "calculadora-multa-sii", sueldo: "calculadora-impuesto-unico", conv: "conversor-uf-utm-dolar" };
function panel() {
  const s = SIMS[actual]; valores[actual] ??= {};
  const enlace = document.querySelector("#pag-calc"); if (enlace) enlace.href = "/" + PAGINA[actual];
  $("#panel").innerHTML = `<h3>${s.t}</h3><p class="desc">${s.d}</p><div class="campos">${s.campos.map(([id, lb, ph, op]) => {
    const v = valores[actual][id] ?? (op ? op[0][0] : ph);
    valores[actual][id] = v;
    return `<div><label for="c-${id}">${lb}</label>${op
      ? `<select id="c-${id}" data-id="${id}">${op.map(([ov, ol]) => `<option value="${ov}" ${ov === v ? "selected" : ""}>${ol}</option>`).join("")}</select>`
      : `<input id="c-${id}" data-id="${id}" inputmode="decimal" value="${esc(v)}" autocomplete="off">`}</div>`; }).join("")}</div><div id="res"></div>`;
  $("#panel").oninput = (e) => { if (e.target.dataset.id) { valores[actual][e.target.dataset.id] = e.target.value; render(); } };
  render();
}

function render() {
  if (!document.querySelector("#res")) return;
  const r = SIMS[actual].calc(valores[actual] || {});
  $("#res").innerHTML = `<div class="res"><table>${r.filas.map(([a, b]) => `<tr><td>${a}</td><td>${b}</td></tr>`).join("")}${r.total ? `<tr class="total"><td>${r.total[0]}</td><td>${r.total[1]}</td></tr>` : ""}</table></div>
    ${r.nota ? `<p class="fuente">${r.nota}</p>` : ""}<p class="fuente">✅ Fuente: <a href="${r.fuente[1]}" target="_blank" rel="noopener">${r.fuente[0]}</a></p>`;
}

// ---------- calendario ----------
const FERIADOS = ["01-01", "05-01", "05-21", "06-29", "07-16", "08-15", "09-18", "09-19", "10-12", "10-31", "11-01", "12-08", "12-25"];
const esFeriado = (d) => FERIADOS.includes(`${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`);
const habil = (d, atras) => { d = new Date(d); while ([0, 6].includes(d.getDay()) || esFeriado(d)) d.setDate(d.getDate() + (atras ? -1 : 1)); return d; };
const ultimoHabil = (a, m) => habil(new Date(a, m + 1, 0), true);

function calendario() {
  const ini = new Date(hoy.getFullYear(), hoy.getMonth(), hoy.getDate()), fin = new Date(ini); fin.setDate(fin.getDate() + +(document.body.dataset.dias || 60));
  const ev = [];
  for (const a of [ini.getFullYear(), ini.getFullYear() + 1]) {
    for (let m = 0; m < 12; m++) {
      ev.push([habil(new Date(a, m, 20)), "F29 / F50 por internet", "IVA, PPM, retenciones e impuesto único del mes anterior."]);
      ev.push([habil(new Date(a, m, 12)), "F29 en papel", "Plazo para quienes no declaran por internet."]);
      ev.push([new Date(a, m, 10), "Cambia el período de la UF", "Nuevo tramo de valores UF del 10 al 9 del mes siguiente."]);
      if ([3, 5, 8, 10].includes(m)) ev.push([ultimoHabil(a, m), "Contribuciones", "Vence la cuota del impuesto territorial."]);
    }
    ev.push([new Date(a, 3, 1), "Inicio Operación Renta (F22)", "Declaración anual de impuestos a la renta, todo abril."]);
    ev.push([ultimoHabil(a, 3), "Último día Operación Renta", "Plazo final para presentar el F22."]);
    ev.push([new Date(a, 2, 1), "Declaraciones juradas anuales", "En marzo vence la mayoría de las DJ."]);
  }
  const lista = ev.filter(([d]) => d >= ini && d <= fin).sort((x, y) => x[0] - y[0]).slice(0, +(document.body.dataset.eventos || 8));
  $("#cal").innerHTML = lista.map(([d, t, x]) => {
    const dias = Math.round((d - ini) / 864e5);
    const falta = dias === 0 ? "Hoy" : dias === 1 ? "Mañana" : `En ${dias} días`;
    return `<div class="ev"><div class="fecha"><b>${d.getDate()}</b><span>${d.toLocaleDateString("es-CL", { month: "short" })} · ${d.toLocaleDateString("es-CL", { weekday: "short" })}</span></div>
      <div><h4>${t}</h4><p>${x}</p></div><span class="falta ${dias <= 3 ? "pronto" : ""}">${falta}</span></div>`;
  }).join("");
}

// ---------- novedades en vivo ----------
async function novedades() {
  try {
    const r = await fetch("/api/novedades?n=" + (document.body.dataset.n || 4));
    const d = await r.json();
    if (d.error) throw 0;
    const col = (tit, items) => `<div class="nov-col"><h3>${tit}</h3>${items.length ? items.map((i) =>
      `<a class="nov-item" href="${esc(i.url)}" target="_blank" rel="noopener"><b>${esc(i.titulo)}</b><span>${esc(i.detalle).slice(0, 180)}${i.detalle.length > 180 ? "…" : ""}</span></a>`).join("")
      : `<p class="fuente">Sin publicaciones este año.</p>`}</div>`;
    const MES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"];
    const fecha = (s) => { const m = s.match(/(\d{1,2}) de (\w+) del? (\d{4})/i); return m ? new Date(+m[3], MES.indexOf(m[2].toLowerCase()), +m[1]) : 0; };
    const ult = [...d.circulares, ...d.resoluciones].sort((a, b) => fecha(b.titulo) - fecha(a.titulo))[0];
    if (ult) { const f = fecha(ult.titulo), corto = ult.titulo.replace(/Resolución Exenta SII/i, "Res. Ex.").replace(/ del \d.*$/, "");
      $("#ultima").textContent = `${corto} · ${f ? f.toLocaleDateString("es-CL", { day: "numeric", month: "short" }) : ""}`;
      $("#ultima").href = ult.url; $("#ultima").target = "_blank"; $("#ultima").rel = "noopener"; $("#ultima").title = ult.detalle; }
    $("#nov").innerHTML = col("Circulares", d.circulares) + col("Resoluciones", d.resoluciones) + col("Oficios", d.oficios);
    $("#nov-act").textContent = "Actualizado " + new Date(d.actualizado).toLocaleString("es-CL", { dateStyle: "medium", timeStyle: "short" });
  } catch {
    $("#ultima").textContent = "ver en sii.cl"; $("#ultima").href = "https://www.sii.cl/normativa_legislacion/";
    $("#nov").innerHTML = `<p class="fuente">No pude consultar www.sii.cl en este momento. Revisa directamente las <a href="https://www.sii.cl/normativa_legislacion/circulares/" target="_blank" rel="noopener">circulares</a> y <a href="https://www.sii.cl/normativa_legislacion/resoluciones/" target="_blank" rel="noopener">resoluciones</a>.</p>`;
  }
}

tabs(); panel(); indicadores();
if (document.querySelector("#cal")) calendario();
if (document.querySelector("#nov") || document.querySelector("#ultima")) novedades();
