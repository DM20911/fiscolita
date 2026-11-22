---
url: https://www.sii.cl/vat/instructions_v2_english.pdf
titulo: VAT Taxpayers or Withholding Income
categoria: otros
---
VAT Taxpayers or Withholding Income
Tax Taxpayers
Lists to be sent: Instructions

Servicio de Impuestos Internos – SII Chile

CONTENTS
1

Introduction ................................................................................................................................ 2

2

Sending the List ........................................................................................................................... 3

3

2.1

Requirements ............................................................................................................... 3

2.2

Periodicity .................................................................................................................... 3

2.3

List format ................................................................................................................... 4

2.4

List upload.................................................................................................................... 5

2.5

Upload errors ............................................................................................................. 10

2.6

List replacement......................................................................................................... 10

Appendices ................................................................................................................................ 11
3.1

Appendix N°1: File format ......................................................................................... 11

3.2

Appendix N°2: Format validations ............................................................................. 12

1

1 INTRODUCTION
In accordance with current regulation (General Instructions No. 42 of 2020 (Circular No. 42 de
2020)), which provide directions on the taxation and administration regime of Value Added Tax
(VAT) with respect to services rendered by offshore suppliers, and with Directive No. 67 of 2020
(Resolución Ex. SII N° 67 de 2020), which regulates the procedure applicable to offshore suppliers
to declare and pay due VAT, offshore suppliers will be released of charging VAT to a Chilean
beneficiary if such informs his VAT taxpayer status. Likewise, the aforementioned regulations
indicate that services levied with Withholding Income Tax are exempt from VAT according to
article 12, letter E, No. 7 of the Law on Sales and Services Tax, so the offshore supplier should not
charge VAT to the Chilean beneficiary.
In both cases, it is the sole responsibility of the service beneficiary to inform the offshore supplier
about his VAT taxpayer status, or that services are taxed with Withholding Tax. The beneficiary of
the service or the withholding agent of Withholding Income Tax must inform the offshore supplier
his Tax ID number (RUT). On the other hand, the offshore supplier must periodically send to this
Servicio de Impuestos Internos (SII), in the same month in which he declares and pays due VAT,
the list of service beneficiaries who have not been charged VAT given the information received.
Given the above, the SII makes available to foreign taxpayers without domicile or residence in Chile,
previously registered in the Simplified Tax Regime of the new Paragraph 7° bis of the Law on Sales
and Services Tax, an application that will allow them to inform the SII the list of Chilean taxpayers
who have previously communicated their status as VAT taxpayers or if they are withholding agents
of services subject to Withholding Income Tax. Access to this application is through the Digital
VAT Portal, which is available on the SII's website, displayed in English and Spanish.

2

2 SENDING THE LIST
2.1 REQUIREMENTS
To report the list of service beneficiaries to whom VAT was not charged, the offshore supplier must:
1. Be registered in the Digital VAT Portal.
To register, the offshore supplier must access the Digital VAT Portal by entering the “Direct
Access” section of the SII's website, and clicking in the“Registration Form” option.
The registration is successfully completed after having submitted the form, verified the email
and created a password. For more information you can review the step-by-step instructions for
registration available on the Digital VAT Portal, Help section.
2. Have the Tax ID number (RUT) of the service beneficiary to whom VAT was not charged.
It is the sole responsibility of the service beneficiary to inform the offshore supplier of his VAT
taxpayer status or of his withholding agent status of services subject to with Withholding
Income Tax, indicating his Tax ID number (RUT) in order for VAT not to be charged. In the
absence of such information, the offshore supplier must charge VAT to the service beneficary
and not include the Tax ID number (RUT) of the service beneficiary in the list to be sent.

2.2 PERIODICITY
In both cases, the list must be sent according to the periodicity chosen by the offshore supplier
to declare and pay VAT at the time of registration in the Digital VAT Portal.



Monthly periodicity: the offshore supplier must report month by month the list of taxpayers to
which VAT was not charged.
Quarterly periodicity: the offshore supplier must report on fixed quarterly periods (not mobile)
in the following order:
Quarter
1
2
3
4

Months
January, February and March
April, May and June
July, August and September
October, November, December

In both cases, the list must be send in the tax period´s following month and until the last day of such
month.

3

Examples:
a) Monthly periodicity
The deadline to report the list of taxpayers to whom VAT was not charged in January 2024, will
be until February 28, 2024.

b) Quarterly Periodicity
The deadline to report the list of taxpayers to whom VAT was not charged during
January, February and March 2024, will be until April 30, 2024.

2.3 LIST FORMAT
The list to be reported must be contained in a .CSV file, according to the format indicated in
Appendix N ° 1: File Format
There are 4 fields to report, as described below:
Field
Month to report
Tax number (RUT)
DV
Type

Description
Month in which VAT was not charged to the service beneficiary
Tax ID number (RUT) of the service beneficiary that informs his VAT
taxpayer status or his withholding agent status of services taxed with
Withholding Income Tax.
Verification digit
Type of taxpayer to report: VAT or withholding agent of services taxed with
Withholding Income Tax.

Once the information in the .CSV file has been completed and also complying with the validations
of Appendix N ° 2: Format Validations, the offshore supplier can successfully upload the list.

4

2.4 LIST UPLOAD
After assembling the .CSV file, the following steps must be followed to send the list:
1. Enter the option "Sending the List" located in the Digital VAT Portal.
2. Authenticate

3. Period to inform

The selection of the period will depend on the tax period chosen by the offshore supplier to
declare and pay VAT at the time of registration in the Digital VAT Portal. In the case of a monthly
periodicity, the selection will display all the months of the year, and for the case of quarterly
periodicity, four months will be displayed, one per quarter.
Examples:
a) Monthly periodicity
To report the list of taxpayers to whom the VAT was not charged in March 2024, the period
March 2024 must be chosen.

5

b) Quarterly periodicity
To inform the list of taxpayers to whom VAT was not charged during January, February
and March 2024, the period March 2024 must be chosen.
3. Preparing the .CSV file
The file with a .CSV extension must have a maximum of 10 MB to load. Its format is indicated in
Appendix N ° 1 and must comply with the validations of Apppendix N ° 2. It is important to note
that the name of the fields must not be included in the first row.
Example
a) Monthly periodicity
To report a list of 2 service beneficiaries who reported a VAT taxpayer status and a withholding
agent of services subject to a Withholding Tax, respectively, the .CSV file must have the following
format:
202403 1234 5
202403 5678 9

1
2

In this case, it is being informed:
- In the MONTH of March of 2024, the taxpayer service beneficiary with a Tax ID Number
(RUT) 1234-5 reported having a VAT taxpayer status.
- In the MONTH of March of 2024, the taxpayer with Tax ID Number (RUT) 5678-9, reported
being a withholding agent of services taxed with Withhholding Income Tax.
b) Quarterly periodicity
To report a list of 2 service beneficiaries who reported being a VAT taxpayer and a withholding
agent of services taxed with Withhholding Income Tax, respectively, the .CSV file must have the
following format:
202401 1234
202402 1234
202403 1234
202402 5678
202403 5678

5
5
5
9
9

1
1
1
2
2

In this case, it is being informed:
- In the MONTH of January, February and March of 2024, the taxpayer beneficiary of the
service with Tax ID Number (RUT) 1234-5 reported a VAT taxpayer status.
- In the MONTH of February and March 2020, the taxpayer with Tax ID Number (RUT)
5678-9 reported being a withholding agent beneficiary of services taxed with Withholding
Income Tax.
6

4. Uploading information
When selecting the period to report, if there is not a current list loaded, the message "You have
not reported the list of VAT taxpayers or of withholding agents of Withholding Income Tax in this
tax period" will appear.

To load, the .CSV file must be opened by selecting the "browse" button and pressing the
"Load" button.

7

Subsequently, the message “Your list has been received successfully” will appear.

8

To know the result of the load, you can select the period you want to check again, where the
ACCEPTED or REJECTED status will appear.

9

2.5 UPLOAD ERRORS
In the event of errors in the file format the upload will not be possible. Also, if the .CSV file does not
comply with the requested validations, the status "REJECTED" will appear when consulting the
period.

Appendices should be reviewed to correct the record if this situation occurs.

2.6 LIST REPLACEMENT
To correct a list already sent, a new load can be made by selecting the period to replace.

By selecting “Load new list” the new file will replace the previous
one. Any questions should be send to the email box ivasd.chile@sii.cl
10

3 APPENDICES
3.1 APPENDIX N°1: FILE FORMAT
The list to send is made up of a total of 4 columns. The top row with the respective names of each
column should not be considered.
As a summary, each field of the file with the list of beneficiaries who have reported having the status
of VAT taxpayers or being beneficiaries of services subject to Withholding Tax, must comply with
the following structure:
Field Name

Month informed

Tax ID number (RUT)

Verification digit

Type

Description
Month in which VAT was not charged
to the beneficiary of the service.

Format o Codification

NUMERIC
For quarterly periodicity, it is necessary
to report each month in which the tax Coding=YYYYMM
was not charged to the Chilean
taxpayer.
Tax Identity Number (RUT) of the
beneficiary of the service that reports
NUMERIC
his status as a VAT taxpayer or as
withholding agent of services taxed
with Withholding Income Tax.
Verification digit of the Tax ID Number NUMERIC
(RUT) reported
NUMERIC
Type of taxpayer to report

1= VAT Taxpayer
2= Withholding agent of
services
taxed
with
Withholding Income Tax

11

3.2 APPENDIX N°2: FORMAT VALIDATIONS
The following is a summary of the validations that the file with the list of VAT taxpayers or with the
withholding agents of services taxed with Withholding Income Tax must comply:
Name field

Validations



Month informed





Tax ID number (RUT)

Verification digit (DV)




Observations
The month to be reported
must be in YYYYMM
It does not allow the entry of
format,
where
YYYY
characters
corresponds to the year
It does not allow a length different
and MM to the month.
than 6 digits
It does not allow the last two digits
For example, if the month
different from {01, 02, 03, 04, 05, 06,
of October of 2024 is
07, 08, 09, 10, 11, 12}
reported, it should be
Does not allow an empty field
coded 202410.
It does not allow the entry of
characters
It does not allow empty field
It does not allow value 0



Complies with module 11



It does not allow the entry of
characters
It does not allow length greater
than 1 digit
It does not allow digits other than
{1, 2}
It does not allow empty field


Type



Module 11 validation
allows verifying that the
Tax ID Number (RUT)
reported is valid

12
