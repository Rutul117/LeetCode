class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result = []
        line = []
        line_length = 0
        for word in words:
            if line_length + len(word) + len(line) <= maxWidth:
                line.append(word)
                line_length += len(word)
            else:
                extra_spaces = maxWidth - line_length
                if len(line) == 1:
                    result.append(line[0] + ' ' * extra_spaces)
                else:
                    spaces_between_words = extra_spaces // (len(line) - 1)
                    extra_spaces %= (len(line) - 1)
                    justified_line = ''
                    for i in range(len(line) - 1):
                        justified_line += line[i] + ' ' * spaces_between_words
                        if extra_spaces > 0:
                            justified_line += ' '
                            extra_spaces -= 1
                    justified_line += line[-1]
                    result.append(justified_line)
                line = [word]
                line_length = len(word)
        
        last_line = ' '.join(line)
        last_line += ' ' * (maxWidth - len(last_line))
        result.append(last_line)
        
        return result
