"""
QLineEdit：

Functions:
def addAction (action, position)
def addAction (icon, position)

def isReadOnly ()                     # 判断是否只读，返回bool
def setReadOnly (bool)                # 设置是否只读

def text ()                           # 获取编辑框内的文本

def insert (arg__1)                   # 更改文本，插入文本
def inputRejected()                   # 拒绝输入

def echoMode ()                       # 获取回显模式
def setEchoMode (arg__1)              # 设置回显模式

def MaxLength()                       # 获取文本输入框的最大长度
def setMaxLength (arg__1)             # 设置文本输入框最大长度，最大长度为32767

def alignment ()                      # 读取对齐方式
def setAlignment (flag)               # 设置对齐方式

def placeholderText ()                # 获取占位符，返回一个Unicode
def setPlaceholderText (arg__1)       # 设置占位符，arg__1为"str"

def selectedText ()                   # 读取已经选择的文本，返回Unicode
def hasSelectedText ()                # 判断是否有选中的文本，返回bool
def selectionLength ()                # 获取被选文本的长度
def setSelection (arg__1, arg__2)     # 从位置开始和长度字符选择文本。允许负长度。arg__1为开始位置，arg__2为长度。
def selectionEnd ()                   # 获取编辑框中被选文本的最后一个字符的索引，如果没有选择文本，则返回 -1。
def selectionStart ()                 # 获取编辑框中被选文本的第一个字符的索引，如果没有选择文本，则返回 -1。


def del_ ()                           # 如果未选择文本，则删除文本光标右侧的字符。如果选择了任何文本，光标将移动到所选文本的开头并删除所选文本。
def backspace ()                      # 如果未选择文本，则删除文本光标左侧的字符并将光标向左移动一位。如果选择了任何文本，光标将移动到所选文本的开头并删除所选文本。

def completer ()                      # 返回提供完成的当前 QCompleter ？？？
def setCompleter (Qcompleter)         # 设置完成者 ？？？

def createStandardContextMenu ()      # 此函数创建标准上下文菜单，当用户用鼠标右键单击行编辑时会显示该菜单。
                                      # 它是从默认的 contextMenuEvent() 处理程序调用的。弹出菜单的所有权转移给调用者。

def cursorBackward (mark[, steps=1])  # 将光标往回移动steps个字符。如果标记为真，则移动的每个字符都会添加到选择中；如果标记为假，则选择被清除。
def cursorForward(mark[, steps=1])    # 将光标向前移动steps个字符。如果标记为真，则移动的每个字符都会添加到选择中；如果标记为假，则选择被清除。
def cursorMoveStyle ()                # 获取光标移动样式
def setCursorMoveStyle (style)        # 设置光标移动样式
def cursorPosition ()                 # 获取光标位置
def setCursorPosition (int)           # 设置光标位置
def cursorPositionAt (pos)            # 获取指定坐标位置对应文本光标位置？？？
cursorPositionChanged(int, int)       # 光标位置发生发生改变？？？
def cursorRect ()                     # 返回一个包含 LineEdit 光标的矩形？？？
def cursorWordBackward (mark)         # 将光标向后移动一个字。如果mark为真，则该词也被选中
def cursorWordForward (mark)          # 将光标向前移动一个字。如果mark为真，则该词也被选中。

def deselect ()                       # 取消所有被选中的文本
def displayText ()                    # 获取编辑框内显示的文本

def dragEnabled ()                    # 获取当前编辑框是否可以拖动
def setDragEnabled (bool)             # 设置当前编辑框是否可以拖动

def end (mark)                        # 如果光标不在行尾，则将文本光标移动到行尾。如果mark为True，则光标移动前位置到行尾位置的文本将都被选中；
                                      # 如果mark为False，如果移动光标，所有被选中的文本将会变为未选中状态。
def home (mark)                       # 如果光标不在行首，则将文本光标移动到行首。如果mark为True，则光标移动前位置到行首位置的文本将都被选中；
                                      # 如果mark为False，如果移动光标，所有被选中的文本将会变为未选中状态。

def getTextMargins ()                 # 获取编辑框的边距，返回top\bottom\left\right的边距

def hasAcceptableInput ()             # 判断编辑框是否可以接受输入，返回bool
def hasFrame ()                       # 判断编辑框是否有框架，返回bool ???
def setFrame (bool)                   # 设置框架

def initStyleOption (option)          # 使用此 QLineEdit 中的值初始化选项。当子类需要 QStyleOptionFrame ，但又不想自己填写所有信息时，此方法对于子类很有用。

def inputMask ()                      # 获取输入的掩码
def setInputMask (inputMask)          # 设置输入的掩码

def inputMethodQuery (property, argument)  # 输入方法查询 ？？？

def isClearButtonEnabled ()           # 判读是否已启用清除按钮，返回bool
def setClearButtonEnabled (bool)      # 设置清除按钮使能

def isModified ()                     # 判断是否已经修改，返回bool ？？？
def setModified (bool)                # 设置是否修改 ？？？

def isRedoAvailable ()                # 判断重做是否可用，返回bool ？？？
def isUndoAvailable ()                # 判断撤销可用，返回bool ？？？

def textMargins ()                    # 获取文本周围的边距
def setTextMargins (left, top, right, bottom)  # 将框架内文本周围的边距设置为 left、top、right 和 bottom。
def validator ()                      # 返回指向当前输入验证器的指针，如果没有设置验证器，则返回 0。
def setValidator (arg__1)             # 设置检验器


slots:

def setText()                         # 设置编辑框文本内容
def copy()                            # echoMode()是Normal的前提下，将选定的文本复制到剪贴板
def cut()                             # echoMode()是Normal的前提下，将选定的文本复制到剪贴板并删除它。如果当前验证器不允许删除所选文本，则将复制而不删除。
def paste()                           # 在编辑框不是只读情况下,在光标位置插入剪贴板的文本，删除任何选定的文本。如果当前验证器无法接受最终结果，则不能粘贴文本。
def clear()                           # 清除输入的内容
def redo()                            # 如果重做可用，则重做上一个操作 ???
def selectAll ()                      # 选择所有文本（即突出显示它）并将光标移动到末尾。这在插入默认值时很有用，
                                      # 因为如果用户在单击小部件之前键入，则所选文本将被删除。
def undo ()                           # 如果撤消可用，则撤消上一个操作。取消选择任何当前选择，并将选择开始更新到当前光标位置。


signals:

def editFinished()                   # 编辑完成时产生一个信号
def cursorPositionChanged (arg__1, arg__2)  # 光标位置发生变化时产生一个信号
def editingFinished ()               # 当输入完成时产生一个信号。光标移出，按下回车都算输入完成
def inputRejected ()                 # 拒绝输入时产生一个信号
def returnPressed ()                 # 按下回车时产生一个信号
def selectionChanged ()              # 选择的文本发生变化时时产生一个信号
def textChanged (arg__1)             # 编辑框文本发生变化时产生一个信号
def textEdited (arg__1)              # 文本编辑时产生一个信号
"""


