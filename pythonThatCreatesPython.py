#jedenfalls
#04-05-2018
#more files

#quick point, why numbers go up to 255:
#2**8-1


#python IDE
#python interpreter


inp=input("country file name")
f_inp = open(inp,'r')
countries=f_inp.readlines()
f_inp.close()
for country in countries:
  print(country)
  country=country.strip('\n')
  c_file=open("CountryPrograms\hello_"+country+".py",'w')
  line1="module_hello_"+country+".py"
  print(line1,file=c_file)
  line2="print('Hello"+country+"!')"
  print(line2,file=c_file)
  c_file.close()
