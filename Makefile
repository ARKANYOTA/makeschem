makeschem: makeschem.o mappings.o

.o: .c

mappings.c: legacy.json generate-mappings.py
	./generate-mappings.py

.PHONY: clean
clean:
	rm -f makeschem
	rm -f *.o


# ARKANYOTA Part
directory-link:
	ln -sf ~/makeschem/a.schematic ~/.minecraft/schematics/

a:
	./generatedome.py
	./makeschem a.scdef a.schematic

