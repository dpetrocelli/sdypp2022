package org.example;


import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.ArrayList;
import java.util.Random;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class Server {
    // [STEP 1] - Define logger class and configuration
    private final Logger log = LoggerFactory.getLogger(Server.class);
    ServerSocket ss ; 

    public Server(int port) {
        System.out.println("");
        
        try {
            this.ss = new ServerSocket(port);
            log.info ("Server has been started on port:  "+port);
            Socket client;
            // -> 
            // <- 
            BufferedReader br;
            PrintWriter pw;
            Random rand; 
            Integer iterator = 4;
            ArrayList<Thread> threadsMappings = new ArrayList<>();
            //while (true) {
                // client = ss.accept();

                // br = new BufferedReader(new InputStreamReader(client.getInputStream()));
                // //String input = br.readLine();
                // //log.info("nothing");
                // // flush and write instantly
                // pw = new PrintWriter(client.getOutputStream(), true);
                
                // pw.println("esta es mi respuesta: "+new Random().nextInt(1000));
                // Thread.sleep (5000);
                // // force flush (variable = false)
                // pw.flush();
                // log.info("server has been answered client: "+client.getPort() );
                
                // // Close current session
                // pw.close();
                // br.close();
                // client.close();

                Thread shThread;
                for (int i = 0 ; i < iterator ; i ++){
                    shThread = new Thread(new ServerHilo(new Random().ints(100 , 10000).findFirst().getAsInt()));
                    threadsMappings.add(new Thread(new ServerHilo(new Random().ints(100 , 10000).findFirst().getAsInt())));
                    shThread.start();
                    
                }
                // 1
                
                // log.info("TH STATUS: " + shThread.getState());

                // // 3
                // shThread.start();
                // // log.info("TH STATUS: " + shThread.getState());

                // // Thread.sleep(1000);
                // // log.info("TH STATUS: " + shThread.getState());
                // // Thread.sleep(3000);

                // // log.info("TH STATUS: " + shThread.getState());
                // log.info ("papa termino pero espero hijo");
                // while (true) {
                //     if (!(shThread.getState().equals(Thread.State.TERMINATED))) {
                //         log.info("TH STATUS: " + shThread.getState());
                //         Thread.sleep(1000);
                //     }else{
                //         break;
                //     }
                // }
                // threadsMappings.forEach(th -> {
                //     try {
                //         th.join();
                //     } catch (InterruptedException e) {
                //         // TODO Auto-generated catch block
                //         e.printStackTrace();
                //     }
                // }); 
                
                // System.out.println("SIZE: "+threadsMappings.size());
                // threadsMappings.forEach(th -> {
                //     try {
                //         threadsMappings.remove(th);
                //         System.out.println("SIZE: "+threadsMappings.size());
                //         Thread.sleep(100);
                //     } catch (Exception e) {
                //         // TODO Auto-generated catch block
                //         e.printStackTrace();
                //     }
                // }); 

                // while (threadsMappings.size()>0){
                //     for (int i=0; i< threadsMappings.size(); i++){
                //         Thread t = threadsMappings.get(i);
                //         threadsMappings.remove(t);
                        
                //         if (threadsMappings.size()<1){
                //             break;
                //         }
                //         System.out.println("SIZE: "+threadsMappings.size());
                        
                //     }
                // }
                // System.out.println("SIZE: "+threadsMappings.size());    
                log.info ("cierro cuando hijo termino porque pues el join");
                //System.exit(0);                
                
                
         
                

            //}

        } catch (Exception e) {
            log.error("msg: "+e.getMessage());
        }

    }

    public static void main( String[] args )
    {
        // [STEP 0] - Configure variables needed in this resource
        int threadId = (int) Thread.currentThread().getId();
        String logName = Server.class.getSimpleName()+"-"+threadId;
        System.setProperty("log.name", logName);
        System.setProperty("project.name", "Clase1");

        int port = 9090;
        Server server = new Server(port);
    }
}