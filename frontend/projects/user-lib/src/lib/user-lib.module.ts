import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

import { MatListModule } from '@angular/material/list';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatIconModule } from '@angular/material/icon';
import { MatCardModule } from '@angular/material/card';
import { MatButtonModule } from '@angular/material/button';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatMenuModule } from '@angular/material/menu';
import { MatTableModule } from '@angular/material/table';
import { MatSnackBarModule } from '@angular/material/snack-bar'

import { NgxsModule } from '@ngxs/store';

import { ChangePasswordFormComponent } from './components/change-password-form/change-password-form.component';
import { CurrentUserComponent } from './components/current-user/current-user.component';
import { LoginFormComponent } from './components/login-form/login-form.component';
import { UserProfileComponent } from './components/user-profile/user-profile.component';
import { CurrentUserStateService } from './services/current-user-state.service';

export const NgxsFeatureModule = NgxsModule.forFeature([CurrentUserStateService]);

@NgModule({
  declarations: [
    ChangePasswordFormComponent,
    CurrentUserComponent,
    LoginFormComponent,
    UserProfileComponent,
  ],
  imports: [
    CommonModule,
    ReactiveFormsModule,
    HttpClientModule,
    MatListModule,
    MatToolbarModule,
    MatSidenavModule,
    MatButtonModule,
    MatIconModule,
    MatCardModule,
    MatFormFieldModule,
    MatInputModule,
    MatMenuModule,
    MatTableModule,
    MatSnackBarModule,
    NgxsFeatureModule,
  ],
  exports: [
    ChangePasswordFormComponent,
    CurrentUserComponent,
    LoginFormComponent,
    UserProfileComponent,
  ],
})
export class UserLibModule { }
