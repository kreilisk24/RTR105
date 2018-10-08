#!/usr/bin/python
# -*- coding: utf-8 -*-


a = input("Cien. liet., lūdzu, ievadi skaitli: ")
# 3. python'ā visi input rezultāti ir ar str datu tipu
# tāpēc ivadītā lieluma datu tips vēlāk ir jāpārvieto
a = int(a)

# python valoda balstās uz C valodas => print strādā līdzīgi printf
# http://cplusplus.com/reference/cstudio/printf/
print("Liet., Tu esi ievadījis skaitli: %d"%(a))
aa = a * a
print("Tavs skaitlis kvadrātā ir: %d"%(aa))

