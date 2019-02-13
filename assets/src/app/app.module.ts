import { BrowserModule } from '@angular/platform-browser';
import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { HttpClientModule,HTTP_INTERCEPTORS } from '@angular/common/http';
import { RouterModule, Routes } from "@angular/router";
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations'

//Service
import { TokenService } from './commons/services/interceptors/token.service';

//Modules


//Components
// -------
// to create new component type: ng g component (name of component)
// after creating a component, always import it in this module.
// -------
import { AppComponent } from './app.component';



//Pipes


//Routes
const routes: Routes = [
// { path: '', component: (Name of component) },


]


@NgModule({
  declarations: [
  AppComponent

  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    RouterModule.forRoot(routes, {onSameUrlNavigation: 'reload'}),
  ],
  providers: [
  {
    provide: HTTP_INTERCEPTORS,
    useClass: TokenService,
    multi: true
  }
  ],
  bootstrap: [AppComponent],
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})

export class AppModule { }

