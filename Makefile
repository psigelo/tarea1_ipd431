all:
	@mkdir -p latex/img
	@cd CodigoPython; make
	@cd latex; make
	@cd latex; make
	@mv ./latex/tarea1_ipd431_2015.pdf .
	@echo "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n=======================================================================================\nTODO OK!, EL PDF ESTÁ LISTO EN ESTA MISMA CARPETA CON NOMBRE tarea1_ipd431_2015.pdf"

latexOnly:
	@cd latex; make
	@cd latex; make
	@mv ./latex/tarea1_ipd431_2015.pdf .
	@echo "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n=======================================================================================\nTODO OK!, EL PDF ESTÁ LISTO EN ESTA MISMA CARPETA CON NOMBRE tarea1_ipd431_2015.pdf"


git:
	@rm -f *.pdf
	@cd latex; make clean
	@git add --all
	@git status
	@git commit -e
	@git push

clean: 
	@rm -f *.pdf
	@cd latex; make clean
