class Solution:
    def simplifyPath(self, path: str) -> str:
        # Split the input path by '/'
        components = path.split('/')
        stack = []
        
        for component in components:
            if component == '..':  # Parent directory
                if stack:
                    stack.pop()
            elif component == '.' or not component:  # Current directory or empty component
                continue
            else:  # Valid directory or file name
                stack.append(component)
        
        # Join the stack to form the canonical path
        return '/' + '/'.join(stack)
