from collections import defaultdict, deque, namedtuple,Counter
import  json
'''*************************************deque**************************************'''
'''
1.Insertion and deletion from left is additional feature in list'''
ex = deque([1,2,3,4,5,6,7])
print(ex)
ex.appendleft(0)
print(ex)
ex.extendleft([1,23,3])
print(ex)
ex.popleft()
print(ex)
'''******************************defaultdict***************************************'''

''' 1. For nested dicts creates tree'''
ex_1= {"color":{"key":"blue"}, "engine":"samy", "drive":"4 wheel","clearance":225 }
ex_1["color"]["key"]= "red"
print(ex_1)
ex_2 = defaultdict(list,ex_1)
tree= lambda : defaultdict(tree)
some = tree()
some["colors"]["favourites"] = "red"
print(ex_2)
print(some)
print(json.dumps(some))
'''************************************Counter***************************************'''
""
ex_3 = (("cft","vgg"),('vgy',"vggfg"),("vgesa","waeaa"))
asa = [1,3,44,66,66,77,44]
assf = Counter(name for name, colors in ex_3)
aww = Counter(name for name in asa)
print(aww, assf)
'''*********************************namedtuple*****************************************'''
Animal = namedtuple("Animals", "name color")
dog = Animal("rottie","Black")
print(dog.name)
'''**********************************End***********************************************'''


