import urllib.request
class Get_EDetls:
    def Emp_dtls(self):
        contents = urllib.request.urlopen("http://dummy.restapiexample.com/api/v1/employees").read()
        return contents
