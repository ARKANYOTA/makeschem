makeschem: makeschem.o mappings.o

.o: .c

mappings.c: legacy.json generate-mappings.py
	./generate-mappings.py

.PHONY: clean
clean:
	rm -f makeschem
	rm -f *.o

domeandmapclean:
	rm -f averif.png
	rm -f a.png
	rm -f a.scdef
	rm -f dome.schematic
	rm -f map.schematic


# ARKANYOTA Part
directory-link:
	ln -sf ~/makeschem/dome.schematic ~/.minecraft/schematics/
	ln -sf ~/makeschem/map.schematic ~/.minecraft/schematics/

dome:
	./generate.py dome
	./makeschem a.scdef dome.schematic

map:
	./generate.py map
	./makeschem a.scdef map.schematic

