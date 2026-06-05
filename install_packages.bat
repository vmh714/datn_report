@echo off
echo ========================================================
echo   CAI DAT CAC GOI LATEX CAN THIET CHO DO AN (TINYTEX)
echo ========================================================
echo.
echo Dang cap nhat danh sach cac goi...
tlmgr update --self

echo.
echo Dang cai dat khoang 40 goi can thiet...
tlmgr install vntex fancybox enumitem subfiles titlesec chngcntr pdflscape algorithm2e capt-of multirow fancyhdr biblatex biber biblatex-ieee appendix caption listings float xurl glossaries setspace parskip blindtext ifoddpage xspace relsize supertabular hypcap etoolbox koma-script mfirstuc xfor datatool import tracklang geometry graphics psnfss amsmath amsfonts amscls tools

echo.
echo ========================================================
echo   HOAN TAT! BAY GIO BAN CO THE DICH FILE DOAN.TEX
echo ========================================================
pause
