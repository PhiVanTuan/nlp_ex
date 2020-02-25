s="of millions of books from research library collections is justified under the doctrine of fair use under U.S. copyright law."
x=s.split()
def remove_punctation(data):
  if data.startswith('.') or data.startswith(',')or data.startswith('!')or data.startswith('?')or data.startswith(';')or data.startswith(':')or data.startswith('(')or data.startswith(')')or data.startswith('[')or data.startswith(']'):
      data=data[1:]
  if data.endswith('.') or data.endswith(',')or data.endswith('!')or data.endswith('?')or data.endswith(';')or data.endswith(':')or data.endswith('(')or data.endswith(')')or data.endswith('[')or data.endswith(']'):
      data=data[:-1]
  return data
