#!/usr/bin/env python

if __name__ == "__main__":
    taille = 91
    center = 43.5
    rayon = 43
    plusoumoins = 43
    print("Calculating...")
    f = open("a.scdef", "w")
    for x in range(taille):
        for y in range(taille):
            for z in range(taille):
                if (rayon**2)-plusoumoins <round((x-center)**2+(y)**2+(z-center)**2, 2)<=(rayon**2)+plusoumoins:
                    f.write(f"{x} {y} {z} glass\n")
                    n += 1
    f.close()
    print(f"Blocks: {n}")
    print(f"Stacks: {n//64} + {n%64} items")
    print(f"Shulker Boxes: {n//(64*27)} + {(n//64)%27} stacks + {(n%64)} items")
