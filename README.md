# Flowgorithm-Save-File-Parser
Creates Flowgorithm files (.fprg) by parsing pseudo code files (.fgs) removing most initial need for the GUI application when first designing the program. This allows for a faster program design prior to Flowgorithm visual aids for refinement.


<h1>Installation</h1>
<body>
  <p>Download the <code>FG_Parser.py</code> file and place it within your Flowgorithm workspace. <br/>
  </p>
</body>
<h1>Creating a .fprg file from FLOGO-Script</h1>
<body>
  <p>Enter the following command in your terminal:<br/><br/>
     &emsp; <code>python3 FG_Parser.py make YOURFILEGOESHERE.fgs</code><br/><br/>
     This will output the corresponding .fprg file that can be used with the Flowgorithms application.<br/>
  </p>
 </body>
 <h1>Creating files of a different name</h1>
 <body>
  <p>Enter the following commands in your terminal for outputing a .fprg file of a different name from the .fgs file.<br/><br/>
     &emsp; <code>python3 FG_Parser.py -o YOURFGSFILE.fgs OUTPUTFILENAME.fprg</code><br/><br/>
     As you can see, this is supposed to function like compilers like gcc.
  </p>
 </body>
<h1>Input Output Example</h1>
<body>
  <p>Input FOR_LOOP_EXAMPLE.fgs file:</p>
<pre>
    def void() Main(){
          String answer;
	  String customerName;
	  real purchaseAmount;	

	  #Define the Icv and initialize it

	  output("Do you wish to process a customers information? ");
	  input(answer);
          int i;
	  #for Loop testing the Icv
    
	  for(i;(100,10);1){
		  output("Enter the customers name");
		  input(customerName);
		  output("How much did the customer spend");
		  input(purchaseAmount);
		  output("+===================================================================+");
		  output(customerName & "spent" & purchaseAmount & "on the item");
		  output("+===================================================================+");
  
	  	#update Icv answer

	   	output("Do you wish to process a customers information?");
		  input(answer);	
	  }
	  output("end of program");
    }
    def int(ii) cool(int x){
      int ii;
      ii=x;
    }
</pre>
<p>Enter in your terminal: <br/><br/>
  &emsp;<code>python3 FG_Parser.py make forLoopExample.fgs</code><br/><br/>
  Output FOR_LOOP_EXAMPLE.fprg file:
</p>
<pre>
  &lt;?xml version="1.0"?&gt;
&lt;flowgorithm fileversion="2.11"&gt;
   &lt;attributes&gt;
      &lt;attribute name="name" value=""/&gt;
      &lt;attribute name="authors" value="Generated by FlogoScript Parser"/&gt;
      &lt;attribute name="about" value="FlowgoScript Parser is made by JustBobinAround, Check it out on github: https://github.com/JustBobinAround/Flowgorithm-Save-File-Parser"/&gt;
      &lt;attribute name="saved" value="2020-00-00 00:00:00 APM"/&gt;
      &lt;attribute name="created" value="emVsdGVrO3plbHRlay1QQzsyMDIwLTA5LTA5OzA5OjUwOjMwIFBNOzI3ODU="/&gt;
      &lt;attribute name="edited" value="emVsdGVrO3plbHRlay1QQzsyMDIwLTA5LTA5OzEwOjEyOjI2IFBNOzM7Mjg5MA=="/&gt;
   &lt;/attributes&gt;
   &lt;function name="Main" type="None" variable=""&gt;
      &lt;parameters/&gt;
      &lt;body&gt;
         &lt;declare name="answer" type="String" array="False" size=""/&gt;
         &lt;declare name="customerName" type="String" array="False" size=""/&gt;
         &lt;declare name="purchaseAmount" type="Real" array="False" size=""/&gt;
         &lt;comment text="Define the Icv and initialize it"/&gt;
         &lt;output expression="&quot;Do you wish to process a customers information? &quot;" newline="True"/&gt;
         &lt;input variable="answer"/&gt;
         &lt;declare name="i" type="Integer" array="False" size=""/&gt;
         &lt;comment text="for Loop testing the Icv"/&gt;
         &lt;for variable="i" start="100" end="10" direction="inc" step="1"&gt;
            &lt;output expression="&quot;Enter the customers name&quot;" newline="True"/&gt;
            &lt;input variable="customerName"/&gt;
            &lt;output expression="&quot;How much did the customer spend&quot;" newline="True"/&gt;
            &lt;input variable="purchaseAmount"/&gt;
            &lt;output expression="&quot;+===================================================================+&quot;" newline="True"/&gt;
            &lt;output expression="customerName&amp;&quot;spent&quot;&amp;purchaseAmount&amp;&quot;on the item&quot;" newline="True"/&gt;
            &lt;output expression="&quot;+===================================================================+&quot;" newline="True"/&gt;
            &lt;comment text="update Icv answer"/&gt;
            &lt;output expression="&quot;Do you wish to process a customers information?&quot;" newline="True"/&gt;
            &lt;input variable="answer"/&gt;
         &lt;/for&gt;
         &lt;output expression="&quot;end of program&quot;" newline="True"/&gt;
      &lt;/body&gt;
   &lt;/function&gt;
   &lt;function name="cool" type="Integer" variable="ii"&gt;
      &lt;parameters&gt;
         &lt;parameter name="x" type="Integer" array="False"/&gt;
      &lt;/parameters&gt;
      &lt;body&gt;
         &lt;declare name="ii" type="Integer" array="False" size=""/&gt;
         &lt;assign variable="ii" expression="x"/&gt;
      &lt;/body&gt;
   &lt;/function&gt;
&lt;/flowgorithm&gt;
</pre>

<h1>Flogoscript Syntax</h1>
<body>
 <p>Please see the wiki for details on the Flogoscript Syntax:<br/>
  <a href="https://github.com/JustBobinAround/Flowgorithm-Save-File-Parser/wiki">FLOGOSCRIPT WIKI</a></p> 
 </body>
</body>
