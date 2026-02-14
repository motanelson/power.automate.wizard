var1="""SET NewVar TO $'''\"\"'''
LOOP LoopIndex FROM $a0 TO $a15 STEP $a1
    SET NewVar TO $'''%NewVar%  ,  %LoopIndex%'''
END
Display.ShowMessageDialog.ShowMessage Title: $'''hello''' Message: NewVar Icon: Display.Icon.None Buttons: Display.Buttons.OK DefaultButton: Display.DefaultButton.Button1 IsTopMost: False ButtonPressed=> ButtonPressed
"""
print("\033c\033[40;37m\n give me from number? ")
a=input()
print("\033[40;37m\n give me into number ? ")
b=input()
print("\033[40;37m\n give me step number ? ")
c=input()
var1=var1.replace("$a0",a)
var1=var1.replace("$a15",b)
var1=var1.replace("$a1",c)
print("\n"+"-"*80 +"\n")
print(var1)