import time
import pyautogui as m
import random
import pyperclip

def rand(find_button):
	x=random.uniform(find_button['top_left']['x'], find_button['bottom_right']['x'])
	y=random.uniform(find_button['top_left']['y'], find_button['bottom_right']['y'])
	
	return x,y
	
def click():
	num=0
	while num>-1:
		m.click()
		num=num+1
		print(num)
		
		#수강인원 좌표 입력
		population_button={
				'top_left':{'x':1434 , 'y':475},
				'bottom_right':{'x':1435, 'y':476}
		}
		x,y=rand(population_button)
		m.moveTo(x,y,duration=0.1)
		m.click()
		time.sleep(2)
		m.keyDown('Ctrl')
		m.press('c')
		m.keyUp('Ctrl')
		pop=int(float(pyperclip.paste()))
		
		#빨간색 96 대신 전체 수강 정원 입력
		if pop<96:
		#수강신청 버튼 좌표 입력
			apply_button={
					'top_left':{'x':331 , 'y':465 },
					'bottom_right':{'x':387, 'y':482 }
			}
			x,y=rand(apply_button)
			m.moveTo(x,y,duration=0.01)
			m.click()
		else:
		#조회버튼 좌표 입력
			find_button={
					'top_left':{'x':1698,'y':289},
					'bottom_right':{'x':1767,'y':301}
			}	
	
			x,y=rand(find_button)
			m.moveTo(x,y, duration=0.1)
			m.moveTo(x+3,y+3,duration=0.1)
			m.click()
			time.sleep(1)
	return
	
def main():
	try:
	#조회버튼 좌표 입력
		find_button={
				'top_left':{'x':1698,'y':289},
				'bottom_right':{'x':1767,'y':301}
		}	
	
		x,y=rand(find_button)
		m.moveTo(x,y, duration=1)
		click()
		
	except PyperclipWindowsException:
		click()


if __name__ == '__main__':
	main()

