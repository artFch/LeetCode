class BrowserHistory:

    def __init__(self, homepage: str):
        # Initialize list of visited URLs with the homepage
        self.history = [homepage]
        self.currpage = homepage  # Set the current page to the homepage
        self.currpos = 0  # Set the current position in the list to 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.currpos+1]
        self.history.append(url)
        self.currpage = url
        self.currpos = len(self.history) - 1

    def back(self, steps: int) -> str:
        if self.currpos - steps >= 0:
            self.currpos -= steps
        else:
            self.currpos = 0
        self.currpage = self.history[self.currpos]
        return self.currpage

    def forward(self, steps: int) -> str:
        self.currpos = min(self.currpos + steps, len(self.history) - 1)
        self.currpage = self.history[self.currpos]
        return self.currpage
