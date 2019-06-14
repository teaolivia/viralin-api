# viral.in
**[US-EN]**
viral.in is an application to advertise products where there are promotors/referrals who are going to receive points which can be liquidified into their respective balance account. 

**[INA]**
viral.in merupakan aplikasi untuk mengiklankan produk dimana ada promotor / referal yang membantu dalam mempromosikan iklan tersebut, kemudian nantinya referal akan mendapatkan point yang dapat di cairkan dalam bentuk saldo rekening.


|![alt text](https://raw.githubusercontent.com/teaolivia/viral.in/dev-thea/ref/viralin-infrastructure.png)|
|:--:| 
| *viral.in architecture* |


# ! please only make changes in your dev branch

## File Structure
```
--api		/* our backend source */
--ref		/* media resources such as images, logo, media, documents */
--viralin	/* frontend source */
```

### How to push to master
1. Make sure you are currently in ```dev-<yourname>``` branch. If you are currently in ```master```, switch by ```git checkout dev-<yourname>```.
2. ```git add .```
3. ```git commit -m "<message>"```
4. ```git checkout master```
5. ```git pull```
6. ```git checkout <branch_name>```
7. ```git rebase master```
8. ```git checkout master```
9. ```git merge <branch_name>```
10. ```git push```
### Get back to work
11. You are now in branch ```master```. Go back to your dev branch by ```git checkout <branch_name>```
12. Push your changes in your own branch by ```git push```
### Useful git tools
* ```git status```
To check your git current situation, including where branch you at and staged/unstaged changes. Also contains hints what to do next.
* ```git log```
To see past commits and its details. Including commitID
* ```git reset --HARD```
Completely unstage current changes. **!!! ALL YOUR UNSAVED CHANGES WILL BE LOST !!!**
* ```git revert <commit-id>```
Go back to commit with id
