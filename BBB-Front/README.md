# Bbb

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 11.2.6.

## Development server
1 npm install
2 Run `npm start` for a dev server. Navigate to `http://localhost:4200/`. The app will automatically reload if you change any of the source files.

## Code scaffolding

Run `ng generate component component-name` to generate a new component. You can also use `ng generate directive|pipe|service|class|guard|interface|enum|module`.

## Deployment
The project is complete, the dist file has been generated once.But some modifications are to be done for the paths to the back-end application.
The files concerned are: 
*1 proxy.conf.json: modify line 3;  
*2 technical-team.component.html (chemin : 'src/app/Components/club/technical-team/technical-team.component.html) modify line 12; 
*3 galery-detail.component.ts (chemin src/app/Components/galery-detail/galery-detail.component.ts) modify line 38. 
In these three files replace http://localhost:8000 by the address of the back-end.  
 Once the changes have been made and saved, the dist file must be generated.  
  To do this in a terminal, go to the folder (at the root) and type the command ng build --prod.  
   Check if the dist file has been created.Then in Filezilla, configure the host part, username, password and port with the information of the host. Connect.  

     In the right part of Filezilla, you find the remote folders, in the left part the local. In the right part, place yourself in the desired folder (in case of choice of subdomain). In the left part select the folder. In the bottom left corner double click on the dist. folder and select all the content (be careful not to take the folder with the ... ). Drag and drop the folder to the bottom left corner. All the files present locally will be transferred to the remote. Verify that all the files have been transferred at the bottom of filezilla (pending files, failed transfers, successful transfers).  
      In the browser consult the site!