import requests

ascii1 = """ 
·▄▄▄▄▄▄   ▄▄▄· .▄▄ · .▄▄▄  ▄• ▄▌▪  ▄▄▄▄▄        ▄▄▄▄▄▄            ▄▄▌  .▄▄ · 
█  ·▀▄ █·▐█ ▀█ ▐█ ▀. ▐▀•▀█ █▪██▌██ •██   ▄█▀▄   ▀•██ ▀ ▄█▀▄  ▄█▀▄ ██•  ▐█ ▀. 
█▀▀▪▐▀▀▄ ▄█▀▀█ ▄▀▀▀█▄█▌·.█▌█▌▐█▌▐█· ▐█.▪▐█▌.▐▌    ▐█.▪▐█▌.▐▌▐█▌.▐▌██ ▪ ▄▀▀▀█▄
██ .▐█•█▌▐█▪ ▐▌▐█▄▪▐█▐█▪▄█·▐█▄█▌▐█▌ ▐█▌·▐█▌.▐▌    ▐█▌·▐█▌.▐▌▐█▌.▐▌▐█▌ ▄▐█▄▪▐█
▀▀▀ .▀  ▀ ▀  ▀  ▀▀▀▀ ·▀▀█.  ▀▀▀ ▀▀▀ ▀▀▀  ▀█▄▀▪    ▀▀▀  ▀█▄▀▪ ▀█▄▀▪.▀▀▀  ▀▀▀▀ 
By Frasquitow"""



print(ascii1)

versions_data = [
    {
        "version": "1.8.8",
        "link": "https://papermc.io/api/v2/projects/paper/versions/1.8.8/builds/443/downloads/paper-1.8.8-443.jar"
    },
    {
        "version": "1.9.4",
        "link": "https://papermc.io/api/v2/projects/paper/versions/1.9.4/builds/773/downloads/paper-1.9.4-773.jar"
    },
    {
        "version": "1.10.2",
        "link": "https://papermc.io/api/v2/projects/paper/versions/1.10.2/builds/916/downloads/paper-1.10.2-916.jar"
    },
    {
        "version": "1.11.2",
        "link": "https://papermc.io/api/v2/projects/paper/versions/1.11.2/builds/1104/downloads/paper-1.11.2-1104.jar"
    },
    {
        "version": "1.12.2",
        "link": "https://papermc.io/api/v2/projects/paper/versions/1.12.2/builds/1618/downloads/paper-1.12.2-1618.jar"
    },
    {
        "version": "1.13.2",
        "link": "https://papermc.io/api/v2/projects/paper/versions/1.13.2/builds/655/downloads/paper-1.13.2-655.jar"
    },
    {
        "version": "1.14.4",
        "link": "https://papermc.io/api/v2/projects/paper/versions/1.14.4/builds/243/downloads/paper-1.14.4-243.jar"
    },
    {
        "version": "1.15.2",
        "link": "https://papermc.io/api/v2/projects/paper/versions/1.15.2/builds/391/downloads/paper-1.15.2-391.jar"
    },
    {
        "version": "1.16.4",
        "link": "https://papermc.io/api/v2/projects/paper/versions/1.16.4/builds/416/downloads/paper-1.16.4-416.jar"
    },
    {
        "version": "1.17.1",
        "link": "https://papermc.io/api/v2/projects/paper/versions/1.17.1/builds/408/downloads/paper-1.17.1-408.jar"
    },
    {
        "version": "1.18.2",
        "link": "https://api.papermc.io/v2/projects/paper/versions/1.18.2/builds/379/downloads/paper-1.18.2-379.jar"
    },
    {
        "version": "1.19.4",
        "link": "https://api.papermc.io/v2/projects/paper/versions/1.19.4/builds/550/downloads/paper-1.19.4-550.jar"
    },
    {
        "version": "1.20.1",
        "link": "https://api.papermc.io/v2/projects/paper/versions/1.20.1/builds/45/downloads/paper-1.20.1-45.jar"
    }
]


print("Disponible versions:")
for i, version in enumerate(versions_data, start=1):
    print(f"{i}. {version['version']}")


selected_version_index = int(input("\nVersion (Select number): ")) - 1

selected_version = versions_data[selected_version_index]


url = selected_version['link']
filename = url.split("/")[-1]
response = requests.get(url)
with open(filename, "wb") as file:
    file.write(response.content)

print(f"\nSe ha descargado la versión {selected_version['version']} en el archivo {filename}.")

xmx_value = input("Value to Xmx (example 4 for 4Gb): ")
xms_value = input("Ingrese el valor para Xms (example 2 For 2G): ")


start_sh_content = f'''while true
do
java -Xmx{xmx_value}G -Xms{xms_value}G -jar {filename}
echo "If you want to completely stop the server process now, press Ctrl+C before
the time is up!"
echo "Rebooting in:"
for i in 5 4 3 2 1
do
echo "$i..."
sleep 1
done
echo "Rebooting now!"
done
'''


with open('start.sh', 'w') as start_sh_file:
    start_sh_file.write(start_sh_content)

print("\nReady.")


eula_content = 'eula=true'
with open('eula.txt', 'w') as eula_file:
    eula_file.write(eula_content)

print("eula=true.")
print("If you are in ubuntu vps you need give perms start.sh")
print("chmod +x start.sh")
print("to start the server use ./start.sh")
print("if you are in windows only need change the .sh to .bat")
