if [ -d "env" ]
then
  echo -e $"'env' already exists.\n" \
           $"actvate the setup by" $"\e[33m\e[1msource env/bin/activate\e[0m" \
           $"\n\ninstall Python dependencies then by\n" \
           $"\e[33m\e[1mpip install -r requirements.txt\e[0m"
else
  echo -e $"'env' directory is not exist.\n" \
           $"you can install Python virtualenv (and also activate it) by\n" \
           $"\e[33m\e[1mvirtualenv env; source env/bin/activate\e[0m" \
           $"\n\ninstall Python dependencies then by\n" \
           $"\n\e[33m\e[1mpip install -r requirements.txt\e[0m"
fi
