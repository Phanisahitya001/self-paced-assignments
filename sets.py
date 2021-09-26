apps = {"whatsapp","facebook","insta"}
books = {"lightless_sky","wings_of_fire","moon_walk"}
apps.add("mycaptain")
print(apps)
b=books.copy()
print(b)
d=apps.difference(books)
print(d)
apps.discard("facebook")
print(apps)
u=apps.union(books)
print(u)
j1=apps.isdisjoint(books)
print(j1)
books.remove("moon_walk")
print(books)


fruits={"orange","cherry"}
colors={"white","orange"}
i=fruits.intersection(colors)
print(i)
fruits.update(colors)
print(fruits)
j=fruits.isdisjoint(colors)
print(j)
fruits.pop()
print(fruits)


p = {"a", "b", "c"}
q = {"f", "e", "d", "c", "b", "a"}
r = p.issubset(q)
print(r)
s=p.issuperset(q)
print(s)
sd=p.symmetric_difference(q)
print(sd)
