import hashlib

def crack_sha1_hash(hash,use_salts=False):
  passwords_arr = []
  read_and_add_to_arr('top-10000-passwords.txt', passwords_arr)

  passwords_dict = {}
  
  
  if use_salts:
    top_salts_passwords = {}
    top_salts = []
    read_and_add_to_arr("known-salts.txt", top_salts)
    for bsalt in top_salts:
      for bpassword in passwords_arr:
        prepended = hashlib.sha1(bsalt + bpassword).hexdigest()
        appended = hashlib.sha1(bpassword + bsalt).hexdigest()
        top_salts_passwords[prepended] = bpassword.decode('utf-8 ')
        top_salts_passwords[appended] = bpassword.decode('utf-8 ')  
    if hashedLine in top_salts_passwords:
      return top_salts_passwords[hashedLine]
    
  
  for l in passwords_arr:
    hashedLine = hashlib.sha1(l).hexdigest()
    #print(hashedLine)
    passwords_dict[hashedLine] = l.decode('utf-8')
    #print(passwords_dict)

  if hashedLine in passwords_dict:
    return  passwords_dict[hashedLine]
  
  print(passwords_arr)
  return 'PASSWORD NOT IN DATABASE'
  
  
   

def read_and_add_to_arr(file_name, arr):
  with open(file_name, "rb") as combolist:
    line = combolist.readline().strip()
    while line:
      arr.append(line)
      line = combolist.readline().strip()

