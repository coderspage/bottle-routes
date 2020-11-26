from bottle import run, get, post, response


##############################
@get('/')
def render_index():
  return 'index'
  
  
##############################
@get('/users')
def get_users():
  users = [{"id":1, "name":"a"},{"id":2, "name":"b"}]
  return users
  
##############################
@post('/users')
def create_user():
  # Connect to the db
  # Create the command to create an user
  # Execute
  # Try Except
  # Respond with the user's id
  response.status = 200
  response.content_type = 'application/json; charset=UTF-8'
  return '{"id":1}'

##############################
run(host='localhost', port=80, debug=True, reloader=True)















