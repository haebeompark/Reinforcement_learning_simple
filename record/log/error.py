import datetime
class ErrorManagement:
    #singleton desighn pattern
    @staticmethod
    def err(str):
        currentTime = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S  -  ")
        try: 
            f = open("log.txt",'a')
            f.writelines([currentTime,str,"\n"])
        finally:
            f.close()
        