JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64/
cd .. ;
mvn clean package; 
cd target ;
java -jar ex1-0.0.1-SNAPSHOT.jar