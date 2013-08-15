import webapp2


months = ['January',
  'February',
  'March',
  'April',
  'May',
  'June',
  'July',
  'August',
  'September',
  'October',
  'November',
  'December']

  
def valid_month(month):
    for m in months:
        if month.upper() == m.upper():
            return m.capitalize()
    return

def valid_day(day):
    if day and day.isdigit():
        d = int(day)
        if d >= 1 and d <= 31:
            return d
    return

def valid_year(year):
    if year and year.isdigit():
        y = int(year)
        if y > 1900 and y < 2020:
            return y
    return
    
    
form="""
<form method="post">
  What is your birthday? 
  <br>

  <label> Month
    <input type="text" name="month">
  </label>
  <label> Day
    <input type="text" name="day">  
  </label>
  <label> Year
    <input type="text" name="year">  
  </label>
  
  <div style="color: red">%(error)s</div>
  
  <br>
  <br>
  <input type="submit">
</form>
""" 

class MainHandler(webapp2.RequestHandler):
    def write_form(self, error=""):
        self.response.out.write(form % {"error" : error})

    def get(self):
        self.write_form()
        # self.response.out.write(form)
 
       # self.response.headers['Content-Type'] = 'text/plain'
       # self.response.out.write(self.request)
    
    def post(self):
        user_month = valid_month(self.request.get('month')) 
        user_day = valid_day(self.request.get('day'))
        user_year = valid_year(self.request.get('year'))
        
        if not (user_month and user_day and user_year):
            self.write_form("That doesn't look valid to me.")
        else:
            self.response.out.write("Thanks! thats a totally valid day!")
        
app = webapp2.WSGIApplication([
    ('/', MainHandler)],
    debug=True)
