import os
file_path=input("Enter path : ")
files = os.listdir(file_path)

while True:
    print("="*40)
    choose=input('choose bettwen [1,2,3,4] | [e] To exit\n 1-remove \n 2-add \n 3-replace  \n 4-add number before  \n')
    files = os.listdir(file_path)
    
    if choose=="1":
        remove_word=input('remove letter or word:  ')
        for rfile in files:
    
            old_file_path = os.path.join(file_path, rfile)
            new_file_name=rfile.replace(remove_word,"")
            new_file_path = os.path.join(file_path, new_file_name)
            os.rename(old_file_path, new_file_path)
            print(f'{rfile} ===> {new_file_name}')
    
    elif choose=="2":
        added_word =str(input('add letter or word:  '))
        position =int(input('position :  '))
        for dfile in files:
    
            old_file_path = os.path.join(file_path, dfile)
            new_file_name=dfile[:position-1]+added_word+dfile[position-1:]
            new_file_path = os.path.join(file_path, new_file_name)
            os.rename(old_file_path, new_file_path)
            print(f'{dfile} ===> {new_file_name}')
   
    elif choose=="3":
        Old_word =str(input('Old_word :  '))
        New_word =str(input('New_word :  '))
        how_many=int(input('how many you want to replace :'))
        
        if how_many== 1:
            position =int(input('position :  ')) 
            for rpfile in files:
    
                old_file_path = os.path.join(file_path, rpfile)
                new_file_name=rpfile[:position-1]+New_word+rpfile[position:]
                new_file_path = os.path.join(file_path, new_file_name)
                os.rename(old_file_path, new_file_path)
                print(f'{rpfile} ===> {new_file_name}')
       
        elif how_many> 1 or how_many==None:

            for rpfile in files:
            
    
                old_file_path = os.path.join(file_path, rpfile)
                new_file_name=rpfile.replace(Old_word,New_word,how_many)
                new_file_path = os.path.join(file_path, new_file_name)
                os.rename(old_file_path, new_file_path)

    elif choose=="4":
        rstart=int(input('Enter start number'))
        for i, rpfile in enumerate(files, start=rstart):
    
            old_file_path = os.path.join(file_path, rpfile)
            new_file_name=f"{i}-{rpfile}"
            new_file_path = os.path.join(file_path, new_file_name)
            os.rename(old_file_path, new_file_path)
            print(f'{rpfile} ===> {new_file_name}')
        
    elif choose=="e" or "exit":
        print(' {happy to help you} '.center(40,"#"))
        break
    
    else:
        print('You can only choose [1,2,3]')