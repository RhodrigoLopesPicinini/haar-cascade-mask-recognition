import os

def main():

	folder = "positives"
	for count, filename in enumerate(os.listdir(folder)):
		dst = f"withmask_{str(count)}.jpg"
		src =f"{folder}/{filename}" 
		dst =f"{folder}/{dst}"

		os.rename(src, dst)

if __name__ == '__main__':

	main()
