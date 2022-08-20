from collections import namedtuple, Counter

Fish = namedtuple('Fish', ['name', 'especie', 'tanque'])
mi_primer_pez = Fish('Sammy', 'tiburón', 'tanque grande')
print(mi_primer_pez._asdict())


list = [1,2,3,1,1,4,5,4,3,3,3,7,8,7]
print(Counter(list))

estudiantes = 'Nicolás Claudio Brenda Flor Nicolás Flor'.split()
print(Counter(estudiantes))