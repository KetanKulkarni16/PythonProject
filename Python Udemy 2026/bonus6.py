#There are three files and their corrosponding content separate combine them all with each file with specific content


contents =["A carrots are to be sliced longitudinally.","All the carrots were reportedly sliced.","THe slicing process was well presented"]

filenames =["doc.txt","report.txt","presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}",'w')
    file.write(content)