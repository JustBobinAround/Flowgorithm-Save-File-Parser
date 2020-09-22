# Flowgorithm-Save-File-Parser
Creates Flowgorithm files (.fprg) by parsing pseudo code files (.fgs) removing the need for the GUI application


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
     &emps; <code>python3 FG_Parser.py -o YOURFGSFILE.fgs OUTPUTFILENAME.fprg</code><br/><br/>
     As you can see, this is supposed to function like compilers like gcc.
  </p>
 </body>
