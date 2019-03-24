/*
 * This file was automatically generated by EvoSuite
 * Sun Mar 24 15:27:13 GMT 2019
 */

package tutorial;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.util.EmptyStackException;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;
import tutorial.Stack;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true, separateClassLoader = true, useJEE = true) 
public class Stack_ESTest extends Stack_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      Stack<String> stack0 = new Stack<String>();
      Stack<Object> stack1 = new Stack<Object>();
      assertTrue(stack1.isEmpty());
      
      stack1.push(stack0);
      Integer integer0 = new Integer(64);
      stack1.push(integer0);
      stack1.pop();
      assertFalse(stack1.isEmpty());
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      Stack<Object> stack0 = new Stack<Object>();
      assertTrue(stack0.isEmpty());
      
      stack0.push(stack0);
      boolean boolean0 = stack0.isEmpty();
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      Stack<String> stack0 = new Stack<String>();
      // Undeclared exception!
      try { 
        stack0.pop();
        fail("Expecting exception: EmptyStackException");
      
      } catch(EmptyStackException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("tutorial.Stack", e);
      }
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      Stack<String> stack0 = new Stack<String>();
      stack0.push("Stack exceeded capacity!");
      stack0.push("Stack exceeded capacity!");
      stack0.push("Stack exceeded capacity!");
      stack0.push("Stack exceeded capacity!");
      stack0.push("Stack exceeded capacity!");
      stack0.push("Stack exceeded capacity!");
      stack0.push("Stack exceeded capacity!");
      stack0.push("Stack exceeded capacity!");
      stack0.push("Stack exceeded capacity!");
      stack0.push("Stack exceeded capacity!");
      // Undeclared exception!
      try { 
        stack0.push("Stack exceeded capacity!");
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // Stack exceeded capacity!
         //
         verifyException("tutorial.Stack", e);
      }
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      Stack<String> stack0 = new Stack<String>();
      stack0.push((String) null);
      stack0.pop();
      stack0.push((String) null);
      assertFalse(stack0.isEmpty());
      
      stack0.pop();
      boolean boolean0 = stack0.isEmpty();
      assertTrue(boolean0);
  }
}
