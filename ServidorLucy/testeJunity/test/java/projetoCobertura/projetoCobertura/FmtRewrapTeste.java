package projetoCobertura.projetoCobertura;

import static org.junit.Assert.assertTrue;

import org.junit.*;
//import org.junit.jupiter.api.AfterEach;
//import org.junit.jupiter.api.BeforeAll;
//import org.junit.jupiter.api.BeforeEach;
//import org.junit.jupiter.api.Test;

/*
 *

		1 - Coloque o jar do projeto no diretorio bin/
		
		2 - Rode a ferramenta:
		
		java -jar lib/ba-dua-cli-0.4.0-all.jar instrument -dest instr/ -src bin/
		
		Para MACOS:
		 java -cp lib/ba-dua-agent-rt-0.4.0-all.jar:instr FmtRewrapTeste

	 java -cp lib/ba-dua-agent-rt-0.4.0-all.jar: instr FmtRewrapTeste

		 
		 PC normal:
		3 - java -cp lib/ba-dua-agent-rt-0.4.0-all.jar;instr/FmtRewrapTeste.class
		
		java -cp lib/ba-dua-agent-rt-0.4.0-all.jar;instr/FmtRewrapTeste
		
		java -cp lib/ba-dua-agent-rt-0.4.0-all.jar;instr projetoCobertura.projetoCobertura.FmtRewrapTeste
		
		java -cp <Caminho-Projeto-Java>\Ba-dua\lib\ba-dua-agent-rt-0.4.0-all.jar;instr projetoCobertura.projetoCobertura.FmtRewrapTeste

 *
 */
//Tutorial Jacoco falhou
//https://www.mkyong.com/maven/maven-jacoco-code-coverage-example/

public class FmtRewrapTeste {

	public FmtRewrapTeste() {
		// TODO Auto-generated constructor stub
	}
	
    @BeforeClass
    public static void setup() {
        
    }
 
    @AfterClass
    public static void tearDown() {
        
    }
    
	@Test
	public void test() {	
		
		String retorno = FmtRewrap.fmtRewrap("ola mundo \n toasty", 20);
		String testeOutput = "ola mundo   toasty\n";
		
		assertTrue(retorno.compareTo(testeOutput) == 0);
	}

	@Test
	public void test_stringVazia() {	
		
		String testINput = "";
		String testOutput = "\n";

		String retorno = FmtRewrap.fmtRewrap(testINput, 20);
		
		assertTrue(retorno.compareTo(testOutput) == 0);
	}
	
	
	@Test
	public void test_stringCRfim() {	
		
		String testINput = "ola mundo \n";
		String testOutput = "ola mundo  \n";

		String retorno = FmtRewrap.fmtRewrap(testINput, 20);
		
		assertTrue(retorno.compareTo(testOutput) == 0);
	}
	
	@Test
	public void test_stringCRmeio() {	
		
		String testINput = "ola \n mundo ";
		String testOutput = "ola   mundo \n";

		String retorno = FmtRewrap.fmtRewrap(testINput, 20);

		assertTrue(retorno.compareTo(testOutput) == 0);
	}

	
	@Test
	public void test_stringCRInicio() {	
		
		String testINput = "\n ola mundo ";
		String testOutput = "  ola mundo \n";

		String retorno = FmtRewrap.fmtRewrap(testINput, 20);

		assertTrue(retorno.compareTo(testOutput) == 0);
	}
	
	@Test
	public void test_stringCRDuploInicio() {	
		
		String testINput = "\n\n ola mundo ";
		String testOutput = "\n\n ola mundo \n";

		String retorno = FmtRewrap.fmtRewrap(testINput, 20);

		assertTrue(retorno.compareTo(testOutput) == 0);
	}
	
	@Test
	public void test_stringCRDuploMeio() {	
		
		String testINput = "ola \n\n mundo ";
		String testOutput = "ola \n\n mundo \n";

		String retorno = FmtRewrap.fmtRewrap(testINput, 20);

		assertTrue(retorno.compareTo(testOutput) == 0);
	}
	
	@Test
	public void test_stringCRDuploFim() {	
		
		String testINput = "ola mundo \n\n ";
		String testOutput = "ola mundo \n\n \n";

		String retorno = FmtRewrap.fmtRewrap(testINput, 20);

		assertTrue(retorno.compareTo(testOutput) == 0);
	}
	
	@Test
	public void test_stringSemCR() {	
		
		String testINput = "ola mundo";
		String testOutput = "ola mundo\n";

		String retorno = FmtRewrap.fmtRewrap(testINput, 20);
		
		assertTrue(retorno.compareTo(testOutput) == 0);
	}
	
	@Test
	public void test_stringMultiplosCR() {	
		
		String testINput = "ola mundo \n bom dia \n\n adilson lopes \n teste \n";
		String testOutput = "ola mundo   bom\ndia \n\n adilson lopes  \nteste  \n";

		String retorno = FmtRewrap.fmtRewrap(testINput, 20);
		
		assertTrue(retorno.compareTo(testOutput) == 0);
	}

	
}
