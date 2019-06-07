"""Converting noun to plural form. It doesn't support expections"""

str = ['monkey','fly','hero','boy','class']
import re

def plural(noun):
  """Convert noun to plural form"""
  if(re.search('[sxz]$|ch$|sh$',noun)):
    noun += 'es'
    return(noun)

  elif(re.search('[oy]$',noun,re.I)):      
    if(re.search('[aeiou][oy]$',noun,re.I)):
      noun += 's'
    elif(re.search('y$',noun,re.I)):
      noun = noun[:len(noun)-1];
      noun += 'ies'
    else:
      noun += 'es'
    return(noun)

  elif(re.search('(f|fe)$',noun,re.I)):
      noun = noun[:len(noun)-1];
      noun += 'ves'
      return(noun)

  else:
    noun += 's'
    return(noun)

print(plural('leaf'))
