sudo apt update && \
sudo apt upgrade -y && \
sudo apt install -y --no-install-recommends unixodbc curl apt-transport-https gnupg && \
curl https://packages.microsoft.com/keys/microsoft.asc | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/microsoft.gpg && \
curl https://packages.microsoft.com/config/ubuntu/22.04/prod.list | sudo tee /etc/apt/sources.list.d/mssql-release.list && \
sudo apt update && \
ACCEPT_EULA=Y sudo apt install -y msodbcsql18 && \
sudo apt clean