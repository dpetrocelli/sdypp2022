package org.example;

public class ServerHilo implements Runnable {

    Integer sleepTime; 

    public ServerHilo (Integer sleepTime) {
        this.sleepTime = sleepTime;
    }

   

    // -> start viene aca y le da play :)
    @Override
    public void run() {
        Long threadId = Thread.currentThread().getId();
        System.out.println(" Thread ID: " + threadId + " Sleeptime " + this.sleepTime);
        try {
            Thread.sleep(this.sleepTime);
        
        }catch (Exception e) {
            System.out.println(" Nathing");
        }
    }
}
