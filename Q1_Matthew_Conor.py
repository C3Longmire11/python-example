#a.

years_string = "Sam works in a company abc in New York. He joined \
the company last year 2019. Before joining ABC, he used to work for \
a small firm in Arizona. He worked there from 2015 to 2018. Before \
moving to Arizona Sam used to live in South Dakota and he has been \
living there since 2000's."

years_list = []

for i in years_string:
    if i.isdigit() == True:
        years_list.append(i)

years_list = ''.join(years_list)

years_list = years_list[0:4],years_list[4:8],years_list[8:12],\
             years_list[12:16]

print('a. The list of years: ',years_list)

#b.

count_string = years_string.split()
count = 0

for j in count_string:
    if 'abc' in j.lower():
        count += 1

max_val = max(years_list)
min_val = min(years_list)

print ('b. Count: ',count,',','Maximum: ',max_val,',','Minimum: ',min_val)

#c.

print ('c. The new string: ',years_string.lower().replace('h','_'))


with open ("Q1Output.txt","w") as outfile:
    outfile.write('a. The list of years: ' + str(years_list) + '\n')
    outfile.write('b. Count: ' + str(count) + ',' + ' Maximum: ' + str(max_val) +
                  ',' + ' Minimum: ' + str(min_val) + '\n')
    outfile.write('c. The new string: ' + str(years_string.lower().replace('h','_')))
outfile.close()


























