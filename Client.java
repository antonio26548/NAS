package practice1;

import java.util.Arrays;
import java.util.stream.Stream;
import java.io.BufferedWriter;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.net.InetSocketAddress;
import java.net.Socket;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.Scanner;

public class practice {
	
	private static final String SERVER_IP = "127.0.0.1";	//IP주소
	
    public static void main(String[] args) {
    	
    	Socket socket = null;
        socket = new Socket();	//소켓 객체 생성
        String SERVER_PORT = "";
        
        Scanner scanner =new Scanner(System.in);
        
        OutputStream os = null;
        OutputStreamWriter osw = null;
        BufferedWriter bw = null;
        
        InputStream is =null;
        InputStreamReader isr = null;
        BufferedReader br = null;
        
      
        try {
        	 System.out.print("port number: ");
             SERVER_PORT = scanner.nextLine();	//포트 번호
             //서버와 연결
             socket.connect(new InetSocketAddress(SERVER_IP, Integer.parseInt(SERVER_PORT)));
             //서버로 전송을 위한 OutputStream
             os = socket.getOutputStream();
             osw = new OutputStreamWriter(os);
             bw = new BufferedWriter(osw);
             
             //서버로부터 데이터를 받을 InputStream
             is = socket.getInputStream();
             isr = new InputStreamReader(is);
             br = new BufferedReader(isr);
             
                
        	int num; //random 숫자 생성
        	int min; 
        	int max;
        	int[] sortedAnswer;
        	int[] answerList;
        	Scanner in = new Scanner(System.in);
        	System.out.println("choice number of digits : ( 2,3,4 )");
        	int vNum = in.nextInt();
        	if( vNum == 2 ){
        		min = 10;
        		max = 100;
        		num = (int)((Math.random() * (max - min)) + min);
        		sortedAnswer = Stream.of(String.valueOf(num).split("")).mapToInt(Integer::parseInt).toArray();  //정답을 순서대로 나타내는 리스트
        		answerList = Stream.of(String.valueOf(num).split("")).mapToInt(Integer::parseInt).toArray(); //정답을 그대로 나타내는 리스트
        		Arrays.sort(sortedAnswer);
        		int count = play(num,sortedAnswer,answerList);
        		
        		 bw.write(count);

                 bw.newLine();
                 bw.flush();
		
        	}
        	else if( vNum == 3 ){
        		min = 100;
        		max = 1000;
        		num = (int)((Math.random() * (max - min)) + min);
        		sortedAnswer = Stream.of(String.valueOf(num).split("")).mapToInt(Integer::parseInt).toArray();
        		answerList = Stream.of(String.valueOf(num).split("")).mapToInt(Integer::parseInt).toArray();
        		Arrays.sort(sortedAnswer);
            	int count = play(num,sortedAnswer,answerList);
            	bw.write(count);
                bw.newLine();
                bw.flush();
        	}
        	else if( vNum == 4 ){
        		min = 1000;
        		max = 10000;
        		num = (int)((Math.random() * (max - min)) + min);
            	sortedAnswer = Stream.of(String.valueOf(num).split("")).mapToInt(Integer::parseInt).toArray();
            	answerList = Stream.of(String.valueOf(num).split("")).mapToInt(Integer::parseInt).toArray();
            	Arrays.sort(sortedAnswer);
            	int count = play(num,sortedAnswer,answerList);
            	bw.write(count);
                bw.newLine();
                bw.flush();
        	}
        	else {
        		System.out.println(" error! ");
        	}
		String answerResult;
            answerResult = br.readLine();

            System.out.println("\n");
            if("A".equals(answerResult)) {
            	System.out.println("좋은 실력이네요");
            }
            else if("B".equals(answerResult)) {
            	System.out.println("다음에 더 잘 할 수 있어요");
            }
        	
        }
        catch(IOException e){
            e.printStackTrace();
         }
         finally {
            try {
               if(socket != null && !socket.isClosed()) {
                  socket.close();
               }
            }catch(IOException e){
               e.printStackTrace();
            }
            scanner.close();
         }
    }
    public static int play(int num, int[] sortedAnswer, int[] answerList) {
    	int count = 0;
    	int answer = 0;
    	int s=0,b=0;
    	int[] myAnswer;
    	int length = sortedAnswer.length;
    	while(true) {
            Scanner in = new Scanner(System.in);
            System.out.println("answer list :" + Arrays.toString(sortedAnswer));
            System.out.println(" guess the answer! ");
    		answer = in.nextInt();
    		myAnswer = Stream.of(String.valueOf(answer).split("")).mapToInt(Integer::parseInt).toArray();
    		if(answer != num) {
    			count ++;
    			for(int i = 0; i<length;i++) {
    				if(myAnswer[i] == answerList[i]) {
    					s++;
    				}
    				else {
    					b++;
    				}
    			}
    			System.out.println(" Wrong! ");
    			System.out.println("number of attempts :"+ count);
    			System.out.println("Correct: "+s + " Miss : "+ b);
    			System.out.println("try again!");
    			s=0;b=0;
    		}
    		else {
    			count ++;
    			System.out.println(" Congratulations! You Win! ");
    			System.out.println(" Answer is " +num);
    			System.out.println("number of attempts :"+ count);
    			break;
    		}
		
    	}
    	return count;
    }
}

