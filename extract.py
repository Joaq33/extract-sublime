import sublime
import sublime_plugin
import re

class IntroduceVariableCommand(sublime_plugin.TextCommand):

    var_name = "NewVar"

    def run(self, edit):

        sels = self.view.sel()

        for sel in sels:  
            if not sel.empty():
                sel_text    = self.view.substr(sel)
                top_line    = self.view.lines(sel)[0]
                top_line_text = self.view.substr(top_line)
                indentation = ""

                match = re.search(r"\W*", top_line_text, re.UNICODE)

                if match:
                    indentation = match.group(0)

                var_declaration = indentation + self.var_name + " = " + sel_text + ",\n"

                self.view.replace(edit, sel, self.var_name)

                self.view.insert(edit, top_line.a, indentation) 