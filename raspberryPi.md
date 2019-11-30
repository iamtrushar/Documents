## Raspberry Pi 4

 - Install Raspbian using NOOBs OS. Note: takes a while after 100% completion.
 - Enable VCN [youtube](https://www.youtube.com/watch?v=YP3_gvHZhfw) or [link](https://howtoraspberrypi.com/raspberry-pi-vnc/)
   ```
   # run the command 
   sudo raspi-config
   # select the line Interfacing Options, then line VNC, 
   # and finally answer that you want to enable VNC
   ```
 - Install Docker on the pi see instructions [here](https://linuxize.com/post/how-to-install-and-use-docker-on-raspberry-pi/)
 - Pull git repo 
 - Build & run the docker container: 
   ```
   #Build
   docker build -t pi .
   #Run
   docker run -d -p 8080:80 --name forpi pi;
   ```
- Note if need be to stop/delete odl containers
   ```
   docker container stop $(docker container ls -aq);
   docker container rm $(docker container ls -aq)
   ```
- Run Seq server:
  ```
  docker run -d --name seq-server --restart always -e "ACCEPT_EULA=Y" -p 5341:80 datalust/seq:latest;
  ```

 


## Rasberry Pi 4 (Docker Python script)
Side experiment of running python3 file with Docker. Detail instuctions of how to use docker and python [see](https://hub.docker.com/_/python/)
```
docker build -t measure .
docker run -it --rm --name measureScript measure
```
