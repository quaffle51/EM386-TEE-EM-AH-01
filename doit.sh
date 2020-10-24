rm *.log
rm *.aux
rm *.png
rm *.pytxcode
pdflatex pythontex_gallery.tex
pythontex.sh pythontex_gallery
pdflatex pythontex_gallery.tex

