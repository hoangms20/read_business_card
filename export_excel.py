from datetime import datetime
from openpyxl import Workbook

def export_file(list_data):

	#get datetime
	now = datetime.now()
	dt_string = now.strftime("%Y-%m-%d %H-%M-%S")

	wb = Workbook()
	wb['Sheet'].title = "List of Scaner"

	#set heading
	sh1 = wb.active
	sh1['A1'].value = "STT"
	sh1['B1'].value = "Time"
	sh1['C1'].value = "Name"
	sh1['D1'].value = "Job"
	sh1['E1'].value = "Company"
	sh1['F1'].value = "Email"
	sh1['G1'].value = "Phone"
	sh1['H1'].value = "Website"
	sh1['I1'].value = "Address"
	sh1['J1'].value = "Others"

	#write file
	i = 1
	for val in list_data:
		i += 1
		area = ("A" + str(i), "B" + str(i), "C" + str(i), "D" + str(i), "E" + str(i), "F" + str(i), "G" + str(i), "H" + str(i), "I" + str(i), "J" + str(i))
		sh1[area[0]].value = str(i-1)
		sh1[area[1]].value = val[9]
		sh1[area[2]].value = val[1]
		sh1[area[3]].value = val[2]
		sh1[area[4]].value = val[3]
		sh1[area[5]].value = val[4]
		sh1[area[6]].value = val[5]
		sh1[area[7]].value = val[6]
		sh1[area[8]].value = val[7]
		sh1[area[9]].value = val[8]
		

	wb.save("D:\\Python\\business_card_detection\\excel\\" + dt_string + ".xlsx")

if __name__ == "__main__":
	values = [
		("1", "a", "a", "a", "a", "a", "a", "a", "a", "a")
	]
	export_file( values)