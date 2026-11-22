---
url: https://www.sii.cl/vat/instructions_for_reporting_vendors_and_service_providers.pdf
titulo: Instructions for reporting the list
categoria: otros
---
Instructions for reporting the list
of vendors and service providers
operating through platforms
Requirements for digital intermediation platforms without
domicile or residence in Chile

2025
Servicio de Impuestos Internos – SII Chile

CONTENTS
1

Introduction ................................................................................................................................ 2

2

List Reporting .............................................................................................................................. 3

3

2.1

Requirements ............................................................................................................... 3

2.2

Reporting Frequency .................................................................................................... 3

2.3

List Format ................................................................................................................... 4

2.4

List Upload.................................................................................................................... 4

2.5

Upload Errrors .............................................................................................................. 8

2.6

List Replacement .......................................................................................................... 8

Appendices .................................................................................................................................. 9
3.1

Appendix No. 1: file format .......................................................................................... 9

3.2

Appendix No. 2: format validations ........................................................................... 10

1

1 INTRODUCTION
Pursuant article 3° bis of the Sales and Services Tax Law (hereinafter VAT Law), operators of digital
intermediation platforms (hereinafter platforms) are deemed as the seller or service provider and
thus are liable for VAT that levies sales and services concluded through their platforms. Therefore,
they must charge VAT to the purchaser or beneficiary of the service, declare and pay VAT through
the Digital VAT Form (F129).
Notwithstanding the foregoing, the platform operator is released from the obligation to charge,
declare and pay VAT levied on the sale or the provision of services when the seller or the service
provider has informed that he is a VAT taxpayer in Chile, through the channel provided by the
operator for this purpose.
However, and despite not being liable for VAT, platform operators without domicile or residence in
Chile must comply with the obligation referred to in the second paragraph of article 35 I of the VAT
Law, that is, to provide the information available to them regarding the identification of all Chilean
resident or domiciled sellers and service providers using their platforms, whether they have
reported having a VAT taxpayer status in Chile or not, and the sums paid or made available to them
by the platform.
Indeed, the reporting obligation imposed by the article cited in the previous paragraph applies to all
transactions carried out through platforms, regardless of the amount or the status of the parties
involved.
In light of the above, the Servicio de Impuestos Internos of Chile (SII) has implemented an
application that will allow platform operators previously registered in the Simplified Tax Regime to
submit the list of vendors and service providers operating through their platforms, identifying
whether they are VAT taxpayers in Chile or not. This application can be accessed through the Digital
VAT Portal (hereinafter, Portal), which is available on the SII website (www.sii.cl).

2

2 LIST REPORTING
2.1 REQUIREMENTS
To report the list of vendors and service providers operating through a platform without domicile
or residence in Chile, the platform operator must:
1. Be registered in the Simplified Tax Regime
To register for the Simplified Tax Regime, platform operators must access the Digital VAT Portal
located in the "Direct Access" section of the SII website (www.sii.cl). Once in the Portal the
"Registration Form" option must be clicked.
Registration is completed after submitting the Form, verifying the email address provided and
creating a password. For more information, please review SII Directive N° 84 of 2025 and the
step-by-step instructions available in the "Help and Document" section of the Portal.
2. Have the name or business name of the seller or service provider and his respective Rol Único
Tributario (RUT), which is the Chilean Tax ID.
According to article 35 I of the VAT Law, operators of digital intermediation platforms must
provide information on all sellers and service providers using their platforms, whether they have
reported their status as VAT taxpayers or not, and the amounts paid to them or made available
to them. It is the sole responsibility of the seller or service provider to inform the platform of
his VAT status, indicating the name of the business and RUT.
If the seller or service provider fails to comply with this obligation, the platform must recharge
and pay the VAT associated with the transaction.

2.2 REPORTING FREQUENCY
The list must be reported twice a year: the information for the first half of the year (January – June)
must be sent by the last business day of August of the same year. The list for the second half of the
year (July – December) must be reported by the last business day of February of the following year.
Considering the effective date of the new regulations (October 25, 2025), on a temporary and only
one-time basis, the first list must be submitted on the last business day of August 2026 and must
include information for the months of October, November and December 2025, as well as
information for the semester January – June 2026. For the purposes of uploading the first list, the
January – June 2026 semester must be selected, as shown in section 2.4 of this Instructions.

3

2.3 LIST FORMAT
The list to be reported must be contained in a .CSV file, as indicated in Appendix No 1: File Format.
The fields to be reported are described below:
Field

Description

Year and month

Year and month of the transaction

RUT

Seller or service provider's RUT (Chilean Tax ID)

DV

Verification digit of the seller or service provider's RUT

Type

Binary field (1, 2) indicating whether the seller or service provider is a VAT
taxpayer or not.

Currency

United States of America dollars (USD), euros (EUR), Chilean pesos (CLP)

Amount

Amount (USD, EUR or CLP) paid or made available to the seller or service
provider.

Once the information in the .CSV file has been completed and the validations of Appendix No. 2:
Format Validations have been performed, the platform can upload the list.

2.4 LIST UPLOAD
After creating the .CSV file, please follow these steps to send the list:
1. Go to the "Sending Lists" option in the Digital VAT

2. Authenticate

4

3. Reporting period
For example, if you want to upload a list of vendors or service providers who operated through the
platform during the first half of 2026, you should select the January – June semester and then the
year 2026.

4. Prepare the .CSV file
The file with a .CSV extension must be 10 MB or less for uploading. The file format must correspond
to that shown in Appendix No. 1 and must comply with the validations shown in Appendix No. 2.
The field names should not be included in the first row.
Example:

To report a list for three sellers or service providers who operated on a platform in a given
period, the .CSV file must have the following format:
202602 1234 5
202608 5678 9
202610 9123 7

1
2
1

CLP 500000,00
USD 30000,00
EUR 20000,00

In this case, the following is being reported:
- In February 2026, the seller or service provider with RUT 1234-5 reported being a VAT
taxpayer and received a payment of five hundred thousand Chilean pesos.
- In August 2026, the seller or service provider with RUT 5678-9 received a payment of
thirty thousand United States of América dollars.
- In October 2026, the vendor or service provider with RUT 9123-7 reported being a VAT
taxpayer and received a payment of twenty thousand euros.

5

5. Upload information
When selecting the semester and year to report, if there is no current list uploaded, the message
"You have not reported a list for vendors or service providers in this tax period" will appear.

To upload, open the .CSV file by selecting the browse button and then click "UPLOAD".

6

Once this is done, the message "Your list has been uploaded successfully" will appear.

To see the status of the upload you can select the period you wish to view again. The status will be
ACCEPTED or REJECTED.

7

2.5 UPLOAD ERRORS
If there are errors in the file format, the upload will not be possible. Additionally, if the .CSV file does
not meet the requested validations, the status "REJECTED" will appear when queried.

The Appendices should be reviewed to correct the file if this situation occurs.

2.6 LIST REPLACEMENT
To correct an already submitted list, you can upload it again by selecting the period to replace it.

Selecting "UPLOAD NEW LIST" will replace the previous one.
Queries should be sent to ivasd.chile@sii.cl

8

3 APPENDICES
3.1 APPENDIX NO. 1: FILE FORMAT
The list to report consists of 6 columns. The top row with the column headings should not be
considered.
Each field in the file must comply with the following structure:
Field Name

Description

Format or Coding

Year and month

Year and month in which the transaction was NUMERIC
carried out.
Coding = YYYYMM

RUT

RUT (Chilean Tax ID number) of the vendor or
NUMERIC
service provider.

DV

Verification digit of the vendor or service
ALPHANUMERIC
provider's RUT.

Type

Binary field (1, 2) indicating whether the NUMERIC
vendor or service provider is a VAT taxpayer 1 = VAT taxpayer
or not.
2 = Non VAT taxpayer

Currency

• United States of America dollars (USD)
• Euros (EUR)
• Chilean pesos (CLP)

Amount

USD and Euros:
NUMERIC,
maximum
2
decimal places, comma as
decimal
separator,
no
Amount (United States of America dollars, thousands separator.
Euros, or Chilean pesos) paid through the
platform to the seller or service provider.
CLP:
NUMERIC,
maximum
2
decimal places, comma as
decimal
separator,
no
thousands separator.

ALPHABETICAL (ISO 4217)

9

3.2 APPENDIX NO. 2: FORMAT VALIDATIONS
The validations that the file must meet are detailed below.
Field Name

Year and month

RUT

Validations

Observations

• Does not allow the entry of characters
• Does not allow lengths other than 6
digits
• Does not allow the last two digits other
than {01, 02, 03, 04, 05, 06, 07, 08, 09,
10, 11, 12}
• Does not allow an empty field

The year and month must
be in the YYYYMM format
where YYYY corresponds
to the year and MM to the
month.
For example, if the month
of November 2025 is
reported, the code should
be 202511.

• Does not allow the entry of characters
• Does not allow an empty field
• Does not allow the value 0

DV

• Complies with modulo 11

Type

• Only allows 1 and 2

Currency

• ISO 4217

Amount

• Greater than 0 and length 15

Validation of module 11
allows verification that
the reported RUT is valid.

10
