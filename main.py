import webbrowser as wb

#A dictionary that contains common covid symptoms
S = {'a':'Headache','b':'Muscle/Body ache','c':'Fever/Chills','d':'Nausea or vomiting','e':'Fatigue','f':'New loss of taste or smell','g':'Diarrhea','h':'Cough'}

#A dictionary that contains the frequently asked questions
Freq ={1:'General questions on Covid-19, the symptoms and how to protect yourself and your loved ones.',2:'Frequently asked questions about the Covid-19 vaccine.'}

a=input("Do you wish to take this survey?")


if a.capitalize() != 'Yes':
  print('Thanks for your time.Have a great one!')

if a.capitalize() == 'Yes':
  print('Thank you!')
  print('\n') 
  print('********************************')
  print('\n') 
  b=input("Do you wish to see a list of covid symptoms:")
  if b.capitalize() == 'Yes':
    print('Symptom 1 is:',S['a'],'\n')
    print('Symptom 2 is:',S['b'],'\n')
    print('Symptom 3 is:',S['c'],'\n')
    print('Symptom 4 is:',S['d'],'\n')
    print('Symptom 5 is:',S['e'],'\n')
    print('Symptom 6 is:',S['f'],'\n')
    print('Symptom 7 is:',S['g'],'\n')
    print('Symptom 8 is:',S['h'],'\n')
    print('\n')

    c=input('Enter the numbers corresponding to your symptoms if none do enter skip:\n') 
    if  c.capitalize() != 'Skip':
      print('We reccommend that you visit a covid test center so that you can get tested for Covid-19')
      d= input('Are you from New York?')

      if d.capitalize() == 'Yes':
        print('Here are some links to covid test centers in the New York area:','\n')
        wb.open_new_tab("https://www.nychealthandhospitals.org/covid-19-testing-sites/")
        print('We hope that this helps. Have a lovely day!')
      else:    
       if d.capitalize() != 'Yes':
        print('Here is a link to covid testing sites for the other states in the US:','\n')
        
        wb.open_new_tab('https://www.hhs.gov/coronavirus/community-based-testing-sites/index.html')
        
        print('We hope that this helps. Have a lovely day!')
    elif c.capitalize() == 'Skip':
      print('Thanks for your time and have a lovely day.')
  
  elif b.capitalize() != 'Yes':
    e =input('Do you have any questions?')

    if e.capitalize() == 'Yes':
      print('Here is a category of frequently asked questions:','\n')    
      print('(1.) ',Freq[1],'\n')
      print('(2.) ',Freq[2],'\n')
      g=input('Which choice best matches your questions (1.) or (.2).If none do enter none.')
      if g.capitalize() == '1':
        print('Here is a link to all issues related to Covid-19 virus:')
        wb.open_new_tab('https://www.cdc.gov/coronavirus/2019-ncov/your-health/index.html')                  
        print('Cheers mate!')
      elif g.capitalize() == '2':
        print('Here is a link to information about the Covid_19 vaccine:')
        wb.open_new_tab('https://www.cdc.gov/coronavirus/2019-ncov/vaccines/faq.html')
        print('Cheers mate!')
      else:
        print('Thanks for your time. Have a good one!')
      


    elif e.capitalize() != 'Yes':
      print('Thanks for your time and have a lovely day.')
    
      
    
      