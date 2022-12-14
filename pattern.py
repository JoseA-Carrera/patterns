import re


def normalize(s):
	replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
		(' ', ''),
		(',', ''),)

	for a, b in replacements:
		s = s.replace(a, b).replace(a.upper(), b.upper())

	return s


def find_pattern(txt: str):
    # 'lenght' se usara como limite
	lenght = len(txt)
	# 'i' sera la indice inicial dentro del string
	i = 0
	# 'l' sera el indice final dentro del instring, van a incrementar ambos en 1 por cada ciclo.
	# También puedes declarar en 'l' la cantidad de caracteres del patrón. En este caso son 4 caracteres
	l = 4

	# 'unique_list' almacenara listas de diferentes patrones
	unique_list = []

	while i <= lenght:
		
		# al estar 'i' en la posicion lenght-3 del string, se dententra el ciclo
		if i == lenght-3:
			break

		# por cada 4 caracteres sumando la posicion en 1, se buscara patrones
		lista = re.findall(txt[i:l], txt)
	
		# en el proceso si hay patrones repetidos se descartara agregarlo a la lista
		if lista not in unique_list:
			unique_list.append(lista)
		l += 1
		i += 1
	
	# la listas dentro de 'unique_list' se convertiran a int
	# su valor sera dependiendo de la cantidad de veces que se repinten su patron
	patterns_index = []

	for list_i in unique_list:
		t = len(list_i)
		patterns_index.append(t)

	# de 'patterns_index' 'pattern_max' obtendra el index del patron que mas se repite
	pattern_max = patterns_index.index(max(patterns_index))
	veces = len(unique_list[pattern_max])

	if veces >= 2:
		print(f'De {txt}')
		print(f"el patron que se repite {veces} veces siendo '{unique_list[pattern_max][0]}' el patron \n")
	else:
		print('no hay patron')

	
consulta = input('escribe una cadena de caracteres: ')
find_pattern(normalize(consulta))
