import os, sys

class Gitup:
	def everything_commited(self):
		res = os.popen("git ls-files --deleted --modified --others --exclude-standard")
		lines = ""
		for line in res.readlines():
			lines += line
			
		if lines == "":
			return 1
		else:
			return 0
	def current_branch(self):
		res = os.popen("git branch")
		lines = []
		current = ""
		for line in res.readlines():
			if line[0:2] == "* ":
				current = line
		return current.split("* ")[1].strip()
	def on_master(self):
		if self.current_branch() == "master":
			return 1
		else:
			return 0
	def gitdown(self):
		if self.on_master():
			print "You are on the master branch. Gitdown is intended to be used in local branches."
			print "git checkout -b yournewbranch to create a new local branch"
			print "or git checkout yourexistingbranch to checkout an existing one."
			os.system("git pull origin master")
			return 0;
		else:
			if(self.everything_commited()):
				self.run_gitdown_commands(self.current_branch())
				print "Finished."
			else:
				os.system("git status")
				_input = raw_input("You have uncommitted changes in "+self.current_branch()+". Do you want to try gitdown anyway? (y/n)\n")
				if(_input.lower() == "y"):
					os.system("git stash")
					self.run_gitdown_commands(self.current_branch())
					os.system("git stash apply")
					print "Finished."
				else:
					print "Ok... coward."
	def gitup(self):
		if(self.everything_commited()):
			self.run_gitup_commands(self.current_branch())
		else:
			os.system("git status")
			_input = raw_input("Warning: You have uncommitted changes. Continue? (y/n)")
			if(_input.lower() == "y"):
				os.system("git stash")
				self.run_gitup_commands(self.current_branch())
				os.system("git stash apply")
			else:
				print "Good girl"
	def run_gitup_commands(self, branch):
		print "Branch: " + branch
		if(branch != "master"):
			os.system("git checkout master")
			os.system("git merge " + branch)
		os.system("git push origin master")
		if(branch != "master"):
			os.system("git checkout " + branch)
			os.system("git rebase master")
		else:
			print "You should really consider doing development locally in a branch that is not the master branch."

	def run_gitdown_commands(self, branch):
		print "Branch: " + branch
		os.system("git checkout master")
		os.system("git pull origin master")
		os.system("git checkout " + branch)
		os.system("git rebase master")
		
if sys.argv[1] == "gitup":
	Gitup().gitup()			
elif sys.argv[1] == "gitdown":
	Gitup().gitdown()	