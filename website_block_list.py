# Something's not working, I was in a rush

file = open("./scam_website_data.csv", "r")
website_list = file.readlines()
website_url = []
for i in range (1, len(website_list)):
	website = website_list[i].split(",")
	website_url.append(str([0][1:][:len(website[0])-2]) + "\n")
file.close()

# Outputs the actual domains to check
file2 = open("./scam_website_url.txt", "w")
for i in range (0, len(website_url)):
	file2.write(str(website_url[i]))